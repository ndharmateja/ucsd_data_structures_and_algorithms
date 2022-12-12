# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def peek(self):
        return self.finish_time[-1]

    def dequeue(self):
        return self.finish_time.pop()

    # Returns the start time of the enqueued request
    def enqueue(self, request: Request):
        # if the queue is empty, the packet will be processed
        # at the time it arrives => start time = arrival time
        # so finish time will be arrival time + process time

        # if queue is not empty, the packet will be processed
        # at the time when the last packet in the queue gets processed
        request_start_time = request.arrived_at if len(
            self.finish_time) == 0 else self.finish_time[0]

        self.finish_time.insert(
            0, request_start_time + request.time_to_process)

        return request_start_time

    def process(self, request: Request):
        # Remove all the completed requests at the time this request comes
        curr_time = request.arrived_at
        while len(self.finish_time) > 0 and self.peek() <= curr_time:
            self.dequeue()

        # If the buffer is full, we cannot process the request
        if len(self.finish_time) == self.size:
            return Response(True, -1)

        # Else, we add the finish time to the queue and
        # return the response with current time
        # (the time at which the request starts processing)
        return Response(False, self.enqueue(request))


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
