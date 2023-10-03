import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;

@SuppressWarnings("unchecked")
public class StronglyConnected {
    private static ArrayList<Integer>[] reverseGraph(ArrayList<Integer>[] adj) {
        int n = adj.length;
        ArrayList<Integer>[] reverse = (ArrayList<Integer>[]) new ArrayList[n];
        for (int i = 0; i < n; i++) {
            reverse[i] = new ArrayList<Integer>();
        }
        for (int v = 0; v < adj.length; v++) {
            for (int neighbour : adj[v]) {
                reverse[neighbour].add(v);
            }
        }
        return reverse;
    }

    // Stack to keep track of the post order while exploring the reverse graph
    private static Stack<Integer> stack = new Stack<>();
    private static Set<Integer> visited = new HashSet<>();

    private static int numberOfStronglyConnectedComponents(ArrayList<Integer>[] adj) {
        // Get the reverse graph
        ArrayList<Integer>[] reverseAdj = reverseGraph(adj);

        // Run DFS on the reverse graph such that the vertices
        // once finished exploring are added to the stack
        // The topmost element in this stack will be the one
        // with the highest post number (source in reverse graph) and
        // the innermost vertex in the stack will be the one
        // with the lowest post number
        for (int v = 0; v < reverseAdj.length; v++) {
            if (!visited.contains(v)) {
                explore(reverseAdj, v, true);
            }
        }

        // Clear visited set to run DFS on the original graph
        visited.clear();

        // As long as the stack is not empty
        // pop the vertex and if it is unvisited, explore it
        // The order in which vertices are explored is, the highest
        // post number vertex (sink in original graph) will be explored
        // first and then the ones with lower post numbers
        int sccCount = 0;
        while (!stack.isEmpty()) {
            int v = stack.pop();
            if (!visited.contains(v)) {
                // Explore the current sink scc completely
                explore(adj, v, false);

                // Increment count as one complete scc is explored
                sccCount++;
            }
        }

        return sccCount;
    }

    private static void explore(ArrayList<Integer>[] adj, int v, boolean isReverse) {
        // Add curr vertex to visited set
        visited.add(v);

        // For each unvisited neighbour of v, explore it
        for (int neighbour : adj[v]) {
            if (!visited.contains(neighbour)) {
                explore(adj, neighbour, isReverse);
            }
        }

        // Add to stack only while exploring the reverse graph
        if (isReverse) {
            stack.push(v);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
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
        System.out.println(numberOfStronglyConnectedComponents(adj));
    }
}
