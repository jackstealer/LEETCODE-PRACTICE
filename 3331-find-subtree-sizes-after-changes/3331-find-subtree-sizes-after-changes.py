
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for node in range(1, n):
            children[parent[node]].append(node)

        # Phase 1: Find the new parent of every node
        new_parent = parent[:]

        last_seen = {}

        # (node, exiting, previous_value)
        stack = [(0, False, -1)]

        while stack:

            node, exiting, previous = stack.pop()
            ch = s[node]

            if not exiting:

                # Find closest ancestor with the same character
                if ch in last_seen:
                    new_parent[node] = last_seen[ch]

                # Save previous value and update dictionary
                previous = last_seen.get(ch, -1)
                last_seen[ch] = node

                # Exit event for backtracking
                stack.append((node, True, previous))

                # Visit children
                for child in reversed(children[node]):
                    stack.append((child, False, -1))

            else:

                # Restore previous dictionary state
                if previous == -1:
                    del last_seen[ch]
                else:
                    last_seen[ch] = previous

        # Phase 2: Build the modified tree
        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            new_children[new_parent[node]].append(node)

        # Get traversal order of the modified tree
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        # Calculate subtree sizes
        ans = [1] * n

        for node in reversed(order):
            if node != 0:
                ans[new_parent[node]] += ans[node]

        return ans
