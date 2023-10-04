import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Bipartite {
    private static int bipartite(ArrayList<Integer>[] adj) {
        // Set to keep track of undiscovered vertices
        HashSet<Integer> undiscovered = new HashSet<>();
        for (int v = 0; v < adj.length; v++) {
            undiscovered.add(v);
        }

        // Coloring to keep track of bipartite
        boolean[] isWhite = new boolean[adj.length];

        // Queue
        Queue<Integer> queue = new LinkedList<>();

        // Outer for loop to go over multiple disconnected components
        for (int v = 0; v < adj.length; v++) {
            // If there is an undiscovered vertex, we can run bfs from that
            // vertex to get all the reachable vertices from this
            if (undiscovered.contains(v)) {

                // Remove v from the undiscovered vertices and mark it as white
                undiscovered.remove(v);
                isWhite[v] = true;

                // Add it to queue
                queue.add(v);

                while (!queue.isEmpty()) {
                    // Get the current vertex
                    int curr = queue.poll();
                    for (int neighbour : adj[curr]) {
                        // If a neighbour is undiscovered
                        // we color it to the opposite of the current vertex
                        // and add it to the queue and remove the neighbour from the undiscovered set
                        if (undiscovered.contains(neighbour)) {
                            queue.add(neighbour);
                            isWhite[neighbour] = !isWhite[curr];
                            undiscovered.remove(neighbour);
                        }
                        // If a neighbour is already discovered and colored the same
                        // as the current vertex, it means that the graph is not bipartite
                        // as adjacent vertices shouldn't have the same color
                        else if (isWhite[curr] == isWhite[neighbour]) {
                            return 0;
                        }

                        // If a discovered neighbour has the opposite color, it is okay
                        // so we don't do anything
                    }
                }
            }
        }

        // If we reach here, we have colored all nodes
        // and there wasn't any problematic edge (for bipartite)
        // So the graph is bipartite
        return 1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] adj = (ArrayList<Integer>[]) new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y;
            x = scanner.nextInt();
            y = scanner.nextInt();
            adj[x - 1].add(y - 1);
            adj[y - 1].add(x - 1);
        }
        scanner.close();
        System.out.println(bipartite(adj));
    }
}
