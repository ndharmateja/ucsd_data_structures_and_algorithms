import java.util.*;

@SuppressWarnings("unchecked")
public class Dijkstra {
    private static long distance(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, int s, int t) {
        // Initialize distance values to infinity
        // and distance of source vertex to 0
        int numVertices = adj.length;
        long[] dist = new long[numVertices];
        for (int v = 0; v < numVertices; v++) {
            dist[v] = Long.MAX_VALUE;
        }
        dist[s] = 0;

        // Intialize priority queue and add all vertices
        // Comparator for this priority queue will be based
        // on the distances of the vertices
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (dist[o1] < dist[o2])
                    return -1;
                if (dist[o1] > dist[o2])
                    return 1;
                return 0;
            }
        });
        for (int v = 0; v < numVertices; v++) {
            pq.add(v);
        }

        // Run as long as the priority queue is not empty and distance
        // of the next extract vertex is not infinity
        // If distance of this extract vertex is infinite
        // it means it is not connected to the source vertex
        // and that means we have run out of vertexs that are connected to s
        // and that means any remaining vertexs (including t)
        // isn't connected to s => we can return -1
        while (!pq.isEmpty() && dist[pq.peek()] != Long.MAX_VALUE) {
            // Get vertex with least distance value from the priority queue
            int curr = pq.poll();
            long currDistance = dist[curr];

            // If the curr vertex is 't' (and dist[t] is not infinite)
            // it means that dist[t] is the shortest distance to t
            // and we can return this distance
            if (curr == t) {
                return currDistance;
            }

            // For each of the neighbours
            // relax the corresponding edge if applicable
            for (int i = 0; i < adj[curr].size(); i++) {
                // Get neighbour and it's weight
                int neighbour = adj[curr].get(i);
                int weight = cost[curr].get(i);

                // Relax the edge from curr to neighbour
                if (dist[neighbour] > currDistance + weight) {
                    // Update the distance of the neighbour
                    dist[neighbour] = currDistance + weight;

                    // Update the priority of neighbour in the priority queue
                    // In java we can only do that by removing and re-inserting
                    // that object
                    pq.remove(neighbour);
                    pq.add(neighbour);
                }
            }
        }

        // We reach here if t isn't present in the graph or
        // if the vertex t isn't connected to the source vertex s
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<Integer>[] adj = (ArrayList<Integer>[]) new ArrayList[n];
        ArrayList<Integer>[] cost = (ArrayList<Integer>[]) new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
            cost[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y, w;
            x = scanner.nextInt();
            y = scanner.nextInt();
            w = scanner.nextInt();
            adj[x - 1].add(y - 1);
            cost[x - 1].add(w);
        }
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        scanner.close();
        System.out.println(distance(adj, cost, x, y));
    }
}
