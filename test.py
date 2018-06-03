
def 4sum(self, nums):

    left = 0
    right = len(nums) - 1
    res = []

    nums = sorted(nums)

    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j != i + 1 and nums[j] == nums[j-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[j] + nums[left] + nums[right]

                if temp == target:
                    res.append([i, j, left, right])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                if temp < target:
                    left += 1
                if temp > target:
                    right -= 1
    return res


def validPalindrom(s):

    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            l += 1

        while left < right and not s[right].isalnum():
            r += 1

        if s[left] != s[right]:
            return False
        l += 1
        r -= 1
    return True


def wordBreak(s, wordDict):

    for i in range(len(s) + 1):
        for j in range(0, i):
            if dp[j] and s[j:i] in wordDict:
                possible[i] = True
                break;

    return possible[sLen]


def wordBeak2(s, wordDict):


    def dfs(s, wordDict, dp, res, temp):

        if len(s) == 0:
            res.append(temp)

        for i in range(len(s)):

            if dp[i]:
                temp.append(s[:i+1]):
                dfs(s[i:], wordDict, dp, res, temp):















def maximumPathSum(self, root):


    self.total = 0



def pathSumHelper(self, root):
    left = pathSumHelper(self, root.left)
    right = pathSumHelper(self, root.right)
    temp = max(left + root.val, right + root.val, root.val)

    self.total = max(left + right + root.val, temp. self.total)
    return temp










def isSameTree(p, q):

    if p and q:
        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    else:
        p == q

def isSameTree(p, q):

    queue =  []
    queue.append([p, q])

    while queue:

        node1, node2 = queue.pop(0)

        if not node1 and not node2:
            continue

        elif None in [node1, node2]:
            return False

        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True

def constructTree(preorder, inorder):
        root = Node(preorder[0])
        rootPos = inorder.index(preorder[0])

        root.left = self.constructTree(preorder[1: 1 + rootPos], inorder[:rootPos])
        root.right = self.constructTree(preorder, inorder[rootPos+1:])
        return root

def balancedBSt(root):


    left = self.Depth(root.left)

    right = self.Depth(root.right)

    if left == -1 or right == -1 or Math.abs(left - right) < 1:
        return -1

    return max(left, right)



def Depth(root):

    if root == null:
        return 0

    return max(self.Depth(root.left), self.maxDepth(root.right)) + 1


def populate(self, root):

    stack = []

    queue = [root]

    while stack:

        queue = len(stack):

        for i in range(len(size)):

            if i < size - 1:
                node.next = stack[0]

            else:
                node.next = none

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

def pascals(numRows)

    numRows = [[1]* (i + 1) for i in range(numRows)]

    for i in numRows:
        for j in len(1, i):
            pascals[i][j] = pascals[i-1][j] + pascals[i-1][j-1]

    return pascal


def bestTimeTosellStock(prices):

    f1 = [0] * (len(prices) + 1)

    f2 = [0] * (len(prices) + 1)


    minPrice = prices[0]
    for i in range(1, len(prices)):
        minPrice = min(prices[i], minPrice)
        f1[i] = max(f[i-1], prices[i] - minPrice)

    maxPrice = prices[len(prices) - 1]
    for i in range(len(prices) - 2, -1, -1):
        maxPrices = min(prices[i+1], maxPrices)
        f2[i] = max(maxPrices - prices[i], maxPrices)

    res = 0
    for i in len(f1):
        if f1[i] + f2[i] > res:
            res = f1[i] + f2[i]
    return res

























