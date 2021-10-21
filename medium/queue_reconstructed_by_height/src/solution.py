
class Solution:
    def reconstruct_queue(self, people) -> [[int]]:

        if len(people) <= 1:
            return people

        # ここでは 身長hの大きい順、そしてcurrent以上のhが何人前列にいるかのkでsorting
        # のちに loop比較する際に、事前にh降順にしておくことで
        # 最終的により身長が小さいものが前列にinsert されていくからくり
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        for cur in range(len(people)):
            h, k = people[cur]

            # ここでcurrentの位置がkよりも大きい場合はk値にinsertする
            # このロジックが成立する条件はhが降順になっていることである。
            # ↑↑の前提条件があると
            if k < cur:
                p = people.pop(cur)
                people.insert(k, p)
        return people



