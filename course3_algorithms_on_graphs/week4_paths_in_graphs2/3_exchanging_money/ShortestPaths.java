import java.util.*;

@SuppressWarnings("unchecked")
public class ShortestPaths {
    // Relaxes all edges once in the graph
    // If isVthIteration is true, it also updates the shortest array to 0
    // for nodes whose distance got updated (in the vth iteration)
    private static void relaxAllEdges(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, long[] distance,
            int[] shortest, boolean isVthIteration) {
        for (int u = 0; u < adj.length; u++) {
            for (int j = 0; j < adj[u].size(); j++) {
                int v = adj[u].get(j);
                int uvCost = cost[u].get(j);

                // Relax the edge if dist[u] != inf
                // and if dist[v] is greater than dist[u] + w(u, v)
                if (distance[u] != Long.MAX_VALUE && distance[v] > distance[u] + uvCost) {
                    distance[v] = distance[u] + uvCost;
                    // Mark node v because its distance got updated
                    // in the vth iteration
                    if (isVthIteration) {
                        shortest[v] = 0;
                    }
                }
            }
        }
    }

    private static void shortestPaths(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, int s, long[] distance,
            int[] reachable, int[] shortest) {
        // Init source vertex dist
        distance[s] = 0;

        // Relax all edges for v-1 iterations
        int numVertices = adj.length;
        for (int i = 0; i < numVertices - 1; i++) {
            relaxAllEdges(adj, cost, distance, shortest, false);
        }

        // All the distances that have inf as distance after |V| - 1 iterations
        // are not reachable from s
        // Mark all the nodes who have distance less than inf as reachable
        for (int i = 0; i < distance.length; i++) {
            if (distance[i] < Long.MAX_VALUE) {
                reachable[i] = 1;
            }
        }

        // In the vth iteration, relax all the edges
        // all the nodes that have their dist updated
        // have a path to them with a negative cycle
        // so we mark all of them
        relaxAllEdges(adj, cost, distance, shortest, true);

        // Run BFS from all the nodes whose distance got updated in the vth iteration
        // to find all the reachable nodes from these nodes
        // These nodes (and only these nodes) have infinite arbitrage
        // So we mark the shortest[those nodes] to 0

        // Create queue with all the nodes whose distance got updated
        Queue<Integer> queue = new LinkedList<>();
        for (int v = 0; v < shortest.length; v++) {
            if (shortest[v] == 0) {
                queue.add(v);
            }
        }

        // Run BFS
        // We can use the shortest array to see if we already visited
        // them while going over the neighbours
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int neighbour : adj[curr]) {
                if (shortest[neighbour] != 0) {
                    shortest[neighbour] = 0;
                    queue.add(neighbour);
                }
            }
        }
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
        int s = scanner.nextInt() - 1;
        scanner.close();
        long distance[] = new long[n];
        int reachable[] = new int[n];
        int shortest[] = new int[n];
        for (int i = 0; i < n; i++) {
            distance[i] = Long.MAX_VALUE;
            reachable[i] = 0;
            shortest[i] = 1;
        }
        shortestPaths(adj, cost, s, distance, reachable, shortest);
        for (int i = 0; i < n; i++) {
            if (reachable[i] == 0) {
                System.out.println('*');
            } else if (shortest[i] == 0) {
                System.out.println('-');
            } else {
                System.out.println(distance[i]);
            }
        }
    }

}
