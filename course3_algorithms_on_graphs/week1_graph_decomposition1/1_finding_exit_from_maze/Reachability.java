import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Reachability {
    private static int reach(ArrayList<Integer>[] adj, int x, int y,
            Set<Integer> visited) {
        // Add node 'x' to the visited set
        visited.add(x);

        // Base case: If 'y' is found, we return 1
        if (x == y)
            return 1;

        // For each unvisited neighbour of 'x', find
        // if 'y' can be reached from the neighbour
        // and return 1 if yes
        for (int neighbour : adj[x]) {
            if (!visited.contains(neighbour) && reach(adj, neighbour, y, visited) == 1)
                return 1;
        }

        // If we reach here, 'y' can't be reached from 'x'
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
            adj[y - 1].add(x - 1);
        }
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        scanner.close();

        Set<Integer> visited = new HashSet<>();
        System.out.println(reach(adj, x, y, visited));
    }
}
