import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class JobQueue {
    private int numWorkers;
    private int[] jobs;

    private int[] assignedWorker;
    private long[] startTime;

    private FastScanner in;
    private PrintWriter out;

    static class Thread implements Comparable<Thread> {
        int id;
        long nextFreeTime;

        Thread(int id, long nextFreeTime) {
            this.id = id;
            this.nextFreeTime = nextFreeTime;
        }

        @Override
        public int compareTo(JobQueue.Thread o) {
            if (this.nextFreeTime == o.nextFreeTime) {
                return this.id - o.id;
            }
            return (int) (this.nextFreeTime - o.nextFreeTime);
        }
    }

    public static void main(String[] args) throws IOException {
        new JobQueue().solve();
    }

    private void readData() throws IOException {
        numWorkers = in.nextInt();
        int m = in.nextInt();
        jobs = new int[m];
        for (int i = 0; i < m; ++i) {
            jobs[i] = in.nextInt();
        }
    }

    private void writeResponse() {
        for (int i = 0; i < jobs.length; ++i) {
            out.println(assignedWorker[i] + " " + startTime[i]);
        }
    }

    private void assignJobs() {
        assignedWorker = new int[jobs.length];
        startTime = new long[jobs.length];

        PriorityQueue<Thread> queue = new PriorityQueue<>();

        for (int i = 0; i < numWorkers; i++) {
            queue.add(new Thread(i, 0));
        }

        for (int i = 0; i < jobs.length; i++) {
            int duration = jobs[i];

            Thread bestWorker = queue.poll();
            assignedWorker[i] = bestWorker.id;
            startTime[i] = bestWorker.nextFreeTime;

            bestWorker.nextFreeTime += duration;
            queue.add(bestWorker);
        }
    }

    public void solve() throws IOException {
        in = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        readData();
        assignJobs();
        writeResponse();
        out.close();
    }

    static class FastScanner {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public FastScanner() {
            reader = new BufferedReader(new InputStreamReader(System.in));
            tokenizer = null;
        }

        public String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }
            return tokenizer.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
}
