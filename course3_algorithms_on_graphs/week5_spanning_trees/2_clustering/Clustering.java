import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Clustering {
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

        @Override
        public String toString() {
            return "Point [id=" + id + ", x=" + x + ", y=" + y + "]";
        }
    }

    private static class Edge {
        Point start;
        Point end;
        double length;

        public Edge(Point start, Point end, double length) {
            this.start = start;
            this.end = end;
            this.length = length;
        }

        @Override
        public String toString() {
            return "Edge [start=" + start + ", end=" + end + ", length=" + length + "]";
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

    private static double clustering(int[] xs, int[] ys, int k) {
        // Create the list of edges in ascending order
        int numClusters = xs.length;
        ArrayList<Edge> edges = getSortedEdges(xs, ys);

        // Idea is to keep adding edges (in non-decreasing order)
        // to the existing set of trees (or clusters) in the forest using Kruskal's
        // algorithm until the number of trees (or clusters) get reduced to k
        // and then the answer is the length of the next edge (that has its vertices
        // from different clusters)
        DisjointSets sets = new DisjointSets(xs.length);
        for (Edge edge : edges) {
            // For each edge, if the edge already is in the same tree (or cluster)
            // we don't need to do anything (irrespective of the value of numClusters)

            // If the start and end of edge are in different clusters
            // union them if numClusters > k
            // or if the num clusters == k, return the length of this edge

            // this will ensure that the answer will be the length of the first edge
            // from different clusters after reaching the required number of clusters
            if (sets.find(edge.start.id) != sets.find(edge.end.id)) {
                if (numClusters == k) {
                    return edge.length;
                }

                // at this point numClusters > k
                // and a union will decrease the number of clusters by 1
                sets.union(edge.start.id, edge.end.id);
                numClusters--;
            }

        }

        // We won't reach here as there would be an answer
        // given that k <= num vertices
        return -1;
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
        int k = scanner.nextInt();
        scanner.close();
        System.out.println(clustering(x, y, k));
    }
}
