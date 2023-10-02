import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class ConnectedComponents {
    private static HashSet<Integer> visited = new HashSet<>();

    private static void explore(Integer currVertex, ArrayList<Integer>[] adj) {
        // Add curr vertex to visited
        visited.add(currVertex);

        // Explore all unexplored neighbours
        for (int neighbour : adj[currVertex]) {
            if (!visited.contains(neighbour)) {
                explore(neighbour, adj);
            }
        }
    }

    private static int numberOfComponents(ArrayList<Integer>[] adj) {
        // Number of components
        int numComponents = 0;

        // For each not visited vertex in the graph
        // explore it if it's unexplored
        for (int vertex = 0; vertex < adj.length; vertex++) {
            if (!visited.contains(vertex)) {
                explore(vertex, adj);
                numComponents++;
            }
        }

        // Return number of components
        return numComponents;
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

        System.out.println(numberOfComponents(adj));
    }
}
