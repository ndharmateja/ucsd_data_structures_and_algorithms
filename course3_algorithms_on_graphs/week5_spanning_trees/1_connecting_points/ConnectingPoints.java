import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

@SuppressWarnings("unused")
public class ConnectingPoints {
    private static class DisjointSets {
        private int[] parent;
        private int[] rank;

        public DisjointSets(int n) {
            this.parent = new int[n];
            this.rank = new int[n];
            for (int i = 0; i < n; i++) {
                this.makeSet(i);
            }
        }

        private void makeSet(int i) {
            this.parent[i] = i;
            this.rank[0] = 0;
        }

        private int find(int i) {
            // Without path compression
            // while (i != parent[i]) {
            // i = parent[i];
            // }
            // return i;

            // Using path compression
            if (i != parent[i]) {
                parent[i] = find(parent[i]);
            }
            return parent[i];
        }

        /*
         * unions sets which contain i and j
         * 
         * @return true if i and j were in different sets, false otherwise
         */
        public boolean union(int i, int j) {
            // Get ids of both elements
            int iId = find(i);
            int jId = find(j);

            // If ids of both elements are the same
            // return false
            if (iId == jId)
                return false;

            // Union by rank
            // Attach the smaller tree to the bigger tree
            if (rank[iId] > rank[jId]) {
                parent[jId] = iId;
            } else if (rank[iId] < rank[jId]) {
                parent[iId] = jId;
            } else {
                // If rank of both is same
                // then attach iId's tree to jId
                parent[iId] = jId;
                rank[jId] += 1;
            }

            return true;
        }
    }

    private static class Point {
        int id;
        int x;
        int y;

        public Point(int id, int x, int y) {
            this.id = id;
            this.x = x;
            this.y = y;
        }
    }

    private static class Edge {
        Point start;
        Point end;
        double length;

        public Edge(ConnectingPoints.Point start, ConnectingPoints.Point end, double length) {
            this.start = start;
            this.end = end;
            this.length = length;
        }
    }

    private static double computeDistance(Point p1, Point p2) {
        return computeDistance(p1.x, p1.y, p2.x, p2.y);
    }

    private static double computeDistance(int x1, int y1, int x2, int y2) {
        return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
    }

    private static ArrayList<Edge> getSortedEdges(int[] xs, int[] ys) {
        // For all points (i, j) create an edge and add
        // it to the list of edges
        ArrayList<Edge> edges = new ArrayList<>();
        for (int i = 0; i < xs.length; i++) {
            for (int j = i + 1; j < ys.length; j++) {
                Point start = new Point(i, xs[i], ys[i]);
                Point end = new Point(j, xs[j], ys[j]);
                double distance = computeDistance(start, end);
                Edge edge = new Edge(start, end, distance);
                edges.add(edge);
            }
        }

        // Sort the list of edges based on its length
        Collections.sort(edges, new Comparator<Edge>() {
            @Override
            public int compare(Edge o1, Edge o2) {
                if (o1.length < o2.length)
                    return -1;
                if (o2.length < o1.length)
                    return 1;
                return 0;
            }
        });
        return edges;
    }

    private static double kruskals(int[] xs, int[] ys) {
        // Create the list of edges in ascending order
        double result = 0.;
        ArrayList<Edge> edges = getSortedEdges(xs, ys);

        // Iterate over each of the edges in non-decreasing order
        // and add it to the disjoint sets (if it doesn't form a cycle)
        // If union returns true, it means that edge doesn't form a cycle
        // and is part of the MST, so we add its length to the result
        DisjointSets sets = new DisjointSets(xs.length);
        for (Edge edge : edges) {
            Point start = edge.start;
            Point end = edge.end;
            // We also use ids for the points because
            // of the way DisjointSets data structure was written
            // and it works for integers 0..n-1
            if (sets.union(start.id, end.id)) {
                result += edge.length;
            }
        }

        // Return the sum of edge lengths in the MST
        return result;
    }

    private static PriorityQueue<Integer> initPriorityQueue(double[] cost) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (cost[o1] < cost[o2])
                    return -1;
                if (cost[o2] < cost[o1])
                    return 1;
                return 0;
            }
        });
        return pq;
    }

    private static double prims(int[] xs, int[] ys) {
        // Create result for computing the total weights of MST
        double result = 0.;

        // Initialize all costs to infinity
        double[] cost = new double[xs.length];
        for (int i = 0; i < cost.length; i++) {
            cost[i] = Double.POSITIVE_INFINITY;
        }

        // Select point 0 and make its cost 0
        // and add it to the priority queue
        PriorityQueue<Integer> pq = initPriorityQueue(cost);
        cost[0] = 0;
        pq.add(0);

        // Create a set to track the vertices for which
        // cost is already known
        Set<Integer> visited = new HashSet<>();

        // While the priority queue is non empty
        while (!pq.isEmpty()) {
            // Extract the vertex with the min cost
            // and this will be part of our MST
            // so we add its cost to the result
            // and mark it as visited
            int u = pq.poll();
            result += cost[u];
            visited.add(u);

            // For each of its unvisited neighbours who have
            // a higher cost, we update its cost and also
            // change its priority in the priority queue
            for (int v = 0; v < xs.length; v++) {
                double uvDistance = computeDistance(xs[u], ys[u], xs[v], ys[v]);
                if (!visited.contains(v) && cost[v] > uvDistance) {
                    cost[v] = uvDistance;
                    pq.remove(v);
                    pq.add(v);
                }
            }
        }

        // return the sum of weights in the MST
        return result;
    }

    private static double minimumDistance(int[] xs, int[] ys) {
        return prims(xs, ys);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = scanner.nextInt();
            y[i] = scanner.nextInt();
        }
        scanner.close();
        System.out.println(minimumDistance(x, y));
    }
}
