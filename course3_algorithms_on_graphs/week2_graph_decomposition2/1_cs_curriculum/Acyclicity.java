import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Scanner;

public class Acyclicity {

    // To keep track of all the visited vertices
    private static Set<Integer> visited = new HashSet<>();

    // To keep track of the current path of exploration
    // Becomes empty after complete exploration of a vertex
    // So doesn't need to be reset after every first level explore(v) call
    private static Set<Integer> currentPath = new HashSet<>();

    // returns true if there is a cycle while exploring
    private static boolean explore(ArrayList<Integer>[] adj, int v) {
        // Add current vertex to the visited set
        visited.add(v);

        // Add current vertex to the path of exploration
        currentPath.add(v);

        // For each neighbour
        for (int neighbour : adj[v]) {
            // If the current path of exploration already contains the neighbour
            // that means there is a cycle and we return true
            if (currentPath.contains(neighbour)) {
                return true;
            }

            // We explore an unvisited neighbour
            // and if that call returns true
            // it means that there is a cycle somewhere along the exploration of
            // the neighbour and we return true
            if (!visited.contains(neighbour)) {
                if (explore(adj, neighbour)) {
                    return true;
                }
            }
        }

        // Remove the current vertex from the current path
        currentPath.remove(v);

        // If there was a cycle (completed by a neighbour or
        // during the exploration of a neighbour) we would have already
        // returned true
        // So if we reach here we can return false
        return false;
    }

    private static int acyclic(ArrayList<Integer>[] adj) {
        // Explore each unvisited vertex
        for (int v = 0; v < adj.length; v++) {
            if (!visited.contains(v)) {
                // If exploration of current unvisited vertex returns true
                // it means there is a cycle in this exploration
                // and we return 1
                if (explore(adj, v)) {
                    return 1;
                }

                // After an exploration is completely done
                // the current path set is empty
                // so it can be used for exploring the next unvisited vertex
            }
        }

        // If we reach here that means no cycles and we return 0
        return 0;
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
        }
        scanner.close();
        System.out.println(acyclic(adj));
    }
}
