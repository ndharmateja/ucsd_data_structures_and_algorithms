import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BFS {
    private static int distance(ArrayList<Integer>[] adj, int s, int t) {
        // Initialize all the distances to -1
        // and the distance of s to 0
        int[] distances = new int[adj.length];
        for (int i = 0; i < distances.length; i++) {
            distances[i] = -1;
        }
        distances[s] = 0;

        // Initialize a queue and add the source
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);

        // Run the algo while the queue is not empty
        while (!queue.isEmpty()) {
            // Get the current vertex for processing
            int curr = queue.poll();

            // Go through each undiscovered neighbour (distance is -1 if undiscovered)
            // and add them to queue
            for (int neighbour : adj[curr]) {
                if (distances[neighbour] == -1) {
                    queue.add(neighbour);

                    // distance of neighbour is distance of curr vertex + 1
                    distances[neighbour] = distances[curr] + 1;

                    // If the neighbour is the destination node
                    // we return its distance
                    if (neighbour == t) {
                        return distances[neighbour];
                    }
                }
            }
        }

        // If t is present in the graph we never reach here
        return -1;
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
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        scanner.close();
        System.out.println(distance(adj, x, y));
    }
}
