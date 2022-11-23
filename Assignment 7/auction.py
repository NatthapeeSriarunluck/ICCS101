# Assignment 07, Task 04
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 03:00 hrs

import csv


class Bid:
    def __init__(self, bid_id: int, bidder_id: str, auction: str):
        self.bid_id = bid_id
        self.bidder_id = bidder_id
        self.auction = auction

    def __str__(self):
        return f'Bid ID: {self.bid_id} Bidder ID: {self.bidder_id} Auction: {self.auction}'

    def __repr__(self):
        return f'Bid ID: {self.bid_id} Bidder ID: {self.bidder_id} Auction: {self.auction}'

    def __lt__(self, other):
        return self.bid_id < other.bid_id

    def __gt__(self, other):
        return self.bid_id > other.bid_id

    def __le__(self, other):
        return self.bid_id <= other.bid_id

    def __ge__(self, other):
        return self.bid_id >= other.bid_id

    def __eq__(self, other):
        return self.bid_id == other.bid_id


class Auction:
    def __init__(self, auction):
        self.auction = auction
        self.price = 1
        self.winner = None

    def placeBid(self, bidder_id):
        self.price += 1.5
        self.winner = bidder_id

    def __str__(self):
        return f'Auction (Price: {self.price} Winner: {self.winner})'

    def __repr__(self):
        return f'Auction(Price: {self.price} Winner: {self.winner})'

def CSV2List(csvFilename: str) -> list[Bid]:
    with open(csvFilename, 'r') as files:
        reader = csv.reader(files)
        next(reader)
        ans = []
        for lines in reader:
            ans.append(Bid(int(lines[0]), lines[1], lines[2]))
        return sorted(ans)


def mostPopularAuction(bidList: list[Bid]) -> set[Auction]:
    dic = {}
    for bid in bidList:
        if bid.auction not in dic:
            dic[bid.auction] = [bid.bidder_id]
        else:
            dic[bid.auction].append(bid.bidder_id)
    auctions = {k: list(set(v)) for k, v in dic.items()}
    max_bidders = 0
    ans = set()
    for auction in auctions:
        if len(auctions[auction]) > max_bidders:
            max_bidders = len(auctions[auction])
    for auction in auctions:
        if len(auctions[auction]) == max_bidders:
            ans.add(auction)
    return ans


def auctionWinners(bidList: list[Bid]) -> dict[str, Auction]:
    dic = {}
    for bid in bidList:
        if bid.auction not in dic:
            dic[bid.auction] = [bid]
        else:
            dic[bid.auction].append(bid)
    ans = {}
    for i in dic:
        auc = Auction(dic[i][0])
        for j in dic[i]:
            auc.placeBid(j.bidder_id)
        ans[dic[i][-1].auction] = auc
    sorted_ans = {key: ans[key] for key in sorted(ans.keys())}
    return sorted_ans

