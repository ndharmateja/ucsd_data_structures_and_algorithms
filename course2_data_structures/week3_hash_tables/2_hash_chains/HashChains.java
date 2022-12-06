import java.io.*;
import java.util.StringTokenizer;

public class HashChains {

    private FastScanner in;
    private PrintWriter out;
    private int bucketCount;
    private int prime = 1000000007;
    private int multiplier = 263;

    private Node[] chains;

    static class Node {
        String data;
        Node next;

        Node(String data) {
            this.data = data;
        }
    }

    public static void main(String[] args) throws IOException {
        new HashChains().processQueries();
    }

    private int hashFunc(String s) {
        long hash = 0;
        for (int i = s.length() - 1; i >= 0; --i)
            hash = (hash * multiplier + s.charAt(i)) % prime;
        return (int) hash % bucketCount;
    }

    private Query readQuery() throws IOException {
        String type = in.next();
        if (!type.equals("check")) {
            String s = in.next();
            return new Query(type, s);
        } else {
            int ind = in.nextInt();
            return new Query(type, ind);
        }
    }

    private void writeSearchResult(boolean wasFound) {
        out.println(wasFound ? "yes" : "no");
        // Uncomment the following if you want to play with the program interactively.
        // out.flush();
    }

    private void processQuery(Query query) {
        if (query.type.equals("add")) {
            int index = hashFunc(query.s);
            Node head = chains[index];

            boolean found = isFound(query.s);

            if (found)
                return;

            Node newNode = new Node(query.s);
            if (head == null) {
                chains[index] = newNode;
            } else {
                newNode.next = head;
                chains[index] = newNode;
            }
        } else if (query.type.equals("del")) {
            int index = hashFunc(query.s);

            Node prev = null;
            Node curr = chains[index];

            if (curr == null) {
                return;
            }

            if (curr.data.equals(query.s)) {
                chains[index] = curr.next;
                return;
            }

            while (curr != null) {
                if (curr.data.equals(query.s)) {
                    prev.next = curr.next;
                    break;
                }
                prev = curr;
                curr = curr.next;
            }
        } else if (query.type.equals("find")) {
            writeSearchResult(isFound(query.s));
        } else if (query.type.equals("check")) {
            printChain(query.ind);
        } else {
            throw new RuntimeException("Unknown query: " + query.type);
        }
    }

    private boolean isFound(String s) {
        int index = hashFunc(s);
        Node curr = chains[index];

        while (curr != null) {
            if (curr.data.equals(s)) {
                return true;
            }
            curr = curr.next;
        }

        return false;
    }

    private void printChain(int index) {
        Node curr = chains[index];
        StringBuilder builder = new StringBuilder();
        while (curr != null) {
            builder.append(curr.data);
            builder.append(" ");
            curr = curr.next;
        }
        builder.setLength(Math.max(builder.length() - 1, 0));
        out.println(builder.toString());
    }

    public void processQueries() throws IOException {
        in = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        bucketCount = in.nextInt();

        chains = new Node[bucketCount];

        int queryCount = in.nextInt();
        for (int i = 0; i < queryCount; ++i) {
            processQuery(readQuery());
        }
        out.close();
    }

    static class Query {
        String type;
        String s;
        int ind;

        public Query(String type, String s) {
            this.type = type;
            this.s = s;
        }

        public Query(String type, int ind) {
            this.type = type;
            this.ind = ind;
        }
    }

    static class FastScanner {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public FastScanner() {
            reader = new BufferedReader(new InputStreamReader(System.in));
            tokenizer = null;
        }

        public String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }
            return tokenizer.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
}
