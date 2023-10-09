import java.util.ArrayList;
import java.util.Scanner;

@SuppressWarnings("unchecked")
public class NegativeCycle {
    /**
     * Relaxes all edges once in the graph
     * If isVthIteration is true, and a dist value gets updated
     * it indicates a cycle and true is returned
     * 
     * @param adj
     * @param cost
     * @param distance
     * @param isVthIteration
     * @return true, if in the vth iteration a distance updates, indicating
     *         a negative cycle. returns false otherwise. (Return value is
     *         irrelevant when isVthIteration is false)
     */
    private static boolean relaxAllEdges(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, int[] distance,
            boolean isVthIteration) {
        for (int u = 0; u < adj.length; u++) {
            for (int j = 0; j < adj[u].size(); j++) {
                int v = adj[u].get(j);
                int uvCost = cost[u].get(j);

                // Relax the edge if dist[u] != inf
                // and if dist[v] is greater than dist[u] + w(u, v)
                if (distance[u] != Integer.MAX_VALUE && distance[v] > distance[u] + uvCost) {
                    // If a node's gets updated in the vth iteration
                    // it indicates a negative cycle
                    // and we can return true
                    if (isVthIteration) {
                        return true;
                    }
                    distance[v] = distance[u] + uvCost;
                }
            }
        }

        // Return false if we reach here
        // because there is no negative cycle as none of the
        // dist values got updated in the vth iteration
        // (Only relevant for vth iteration)
        return false;
    }

    /**
     * Runs bellman ford on the graph starting with source as s
     * 
     * @param adj
     * @param cost
     * @param s
     * @param couldHaveCycle
     * @return true if there is a negative cycle along this exploration
     * @return false otherwise, and also updates all the non-infinite nodes'
     *         couldHaveCycle to false
     */
    private static boolean runBellmanFord(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, int s,
            boolean[] couldHaveCycle) {
        // Init distances
        int[] distance = new int[adj.length];
        for (int i = 0; i < distance.length; i++) {
            distance[i] = Integer.MAX_VALUE;
        }
        distance[s] = 0;

        // Relax all edges |V| - 1 times
        int numVertices = adj.length;
        for (int i = 0; i < numVertices - 1; i++) {
            relaxAllEdges(adj, cost, distance, false);
        }

        // If in the vth iteration, relaxAllEdges fn return true
        // it indicates a cycle and we can return true
        if (relaxAllEdges(adj, cost, distance, true))
            return true;

        // There is no negative cycle running bellman ford
        // from source s
        // So we can mark all non infinite vertices' (reachable froms) couldHaveCycle to
        // false because running bellman ford on them also won't produce a cycle
        // (becauses if one of them were to produce a negative cycle, it would have been
        // detected in this call from 's')
        for (int v = 0; v < distance.length; v++) {
            if (distance[v] < Integer.MAX_VALUE) {
                couldHaveCycle[v] = false;
            }
        }

        // Return false as no negative cycle is produced
        return false;
    }

    private static int negativeCycle(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost) {
        // Init boolean array to mark if there could be a cycle with
        // that node as source
        boolean[] couldHaveCycle = new boolean[adj.length];
        for (int v = 0; v < couldHaveCycle.length; v++) {
            couldHaveCycle[v] = true;
        }

        // For each vertex which could have a cycle
        // run bellman ford to see if that source produces a
        // negative cycle
        for (int v = 0; v < couldHaveCycle.length; v++) {
            if (couldHaveCycle[v]) {
                // If runBellmanFord returns true, there definitely is a
                // negative cycle and we can return 1
                // If it returns false, there is no possible negative cycle
                // when starting from vertex v. The fn when returning false
                // also marks all the reachable nodes from v's couldHaveCycle to
                // false because they also won't have negative cycles and we
                // can skip running bellman ford on those nodes
                if (runBellmanFord(adj, cost, v, couldHaveCycle)) {
                    return 1;
                }
            }
        }

        // If we reach here it means no negative cycle was found
        // running bellman ford from any of the vertices
        // so we can return 0
        return 0;
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
        scanner.close();
        System.out.println(negativeCycle(adj, cost));
    }
}
