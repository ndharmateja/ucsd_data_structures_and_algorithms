import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Toposort {
    private static Set<Integer> visited = new HashSet<>();

    private static void swap(ArrayList<Integer> list, int i, int j) {
        int temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }

    private static void reverse(ArrayList<Integer> list) {
        int l = 0;
        int r = list.size() - 1;
        while (l < r) {
            swap(list, l++, r--);
        }
    }

    private static ArrayList<Integer> toposort(ArrayList<Integer>[] adj) {
        ArrayList<Integer> order = new ArrayList<Integer>();
        for (int v = 0; v < adj.length; v++) {
            if (!visited.contains(v)) {
                explore(adj, v, order);
            }
        }

        // Reverse the linear ordering and return it
        reverse(order);
        return order;
    }

    private static void explore(ArrayList<Integer>[] adj, int s, ArrayList<Integer> order) {
        // Add curr vertex to visited set
        visited.add(s);

        // Explore each unvisited neighbour
        for (int neighbour : adj[s]) {
            if (!visited.contains(neighbour)) {
                explore(adj, neighbour, order);
            }
        }

        // Add the curr vertex to the linear ordering
        order.add(s);
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
        ArrayList<Integer> order = toposort(adj);
        for (int x : order) {
            System.out.print((x + 1) + " ");
        }
    }
}
