def findWinner(B: list[str]) -> str:
    test = horizontal(B) + vertical(B) + diagonal(B) + diagonal2(B)
    if 'GGGG' in test:
        return 'G'
    elif 'RRRR' in test:
        return 'R'
    else:
        return '-'


def horizontal(x: list[str]) -> str:
    word = ""
    for i in range(len(x)):
        for j in range(len(x[i])):
            word += x[i][j]
    return word + 'yay'


def vertical(x: list[str]) -> str:
    word = ""
    for i in range(len(x)):
        for j in range(len(x[i])):
            word += x[j][i]
    return word + 'yay'


def diagonal(x: list[str]) -> str:
    word = ""
    for i in range(len(x)):
        for j in range(i + 1):
            word += x[i - j][j]
        word += "-"
    return word


def diagonal2(x: list[str]) -> str:
    word = ""
    for i in range(len(x)):
        for j in range(i + 1):
            word += x[-i - 1 + j][j]
        word += "-"
    return word


def test(B):
    col = len(B[0])
    row = len(B)
    TLBR = [[] for _ in range(row + col - 1)]
    BLTR = [[] for _ in range(len(TLBR))]
    a = -row + 1
    for i in range(col):
        for j in range(row):
            TLBR[i + j].append(B[j][i])
            BLTR[i - j - a].append(B[j][i])
    return TLBR

print(diagonal(['RRRG', '....', 'GRRG', '.R..']))
print(test(['RRRG', '....', 'GRRG', '.R..']))
### Winner ###
assert (findWinner(['RRRG', '....', 'GRRG', '.R..']) == '-')
assert (findWinner(['GRRG', '.GGR', 'GRGR', 'RGRG']) == 'G')
assert (findWinner(['RG..', '....', '....', 'RGR.']) == '-')
assert (findWinner(['RRGG', 'RGRG', 'GR.R', 'GRRG']) == '-')
assert (findWinner(['GR..', '.G..', '..G.', '...G']) == 'G')
assert (findWinner(['GRG.', '.GGG', 'GGGG', 'GGGG']) == 'G')
assert (findWinner(['..RG', '..R.', '..G.', '..G.']) == '-')
assert (findWinner(['R..R', 'RG.R', 'G.GG', '.RRG']) == '-')
assert (findWinner(['R...', '..R.', 'RGG.', '....']) == '-')
assert (findWinner(['RRRR', 'R.R.', 'GRGR', '.GRG']) == 'R')
assert (findWinner(['G..R', '....', '...R', '..GR']) == '-')
assert (findWinner(['GGGR', 'RRGR', 'RRRG', 'GG.G']) == '-')
assert (findWinner(['G.R.', '.G..', 'G...', '..R.']) == '-')
assert (findWinner(['GRGR', 'RRR.', 'GRG.', 'GGGG']) == 'G')
assert (findWinner(['RR..G', 'G....', '.G...', 'R.G..', '.....']) == '-')
assert (findWinner(['GRGR.', 'R.RRR', 'R...R', 'GGGR.', 'GGRRG']) == '-')
assert (findWinner(['.GR..', 'RG...', 'GG.G.', 'RG.R.', '....G']) == 'G')
assert (findWinner(['GG.RG', 'GGRGG', 'GRG..', 'GGRGG', '.RRGR']) == 'G')
assert (findWinner(['..R..', '.GR.R', '.....', '..GG.', '.....']) == '-')
assert (findWinner(['RR..R', '.GRRG', '..RG.', 'RRGG.', '.RRRG']) == 'R')
assert (findWinner(['R..RG', 'RR..R', '.....', '.....', '.R...']) == '-')
assert (findWinner(['RGR.G', 'RRRRR', 'RR.RR', 'GRG.R', 'GR.RG']) == 'R')
assert (findWinner(['.....', 'GG...', 'G..G.', '.R...', '....R']) == '-')
assert (findWinner(['RRR.R', 'GGGGR', 'GGGRR', 'GRGGG', 'RG..G']) == 'G')
assert (findWinner(['...RG', '...R.', '.....', '....R', '.G..G']) == '-')
assert (findWinner(['R.G..', 'GGGGG', 'G.GRG', 'GRRG.', 'GR.GG']) == 'G')
assert (findWinner(['G..RR.', '......', '..R.G.', '.G.RRR', '.RG.R.', '.....R']) == 'R')
assert (findWinner(['RGGGRG', '.RRGR.', 'RRGR..', 'GGRGRG', '.RGG.G', 'G.R.R.']) == 'R')
assert (findWinner(['......', 'GG....', 'G.....', 'GG....', 'GR....', '..G...']) == 'G')
assert (findWinner(['G.GG.G', 'GGR..G', 'GRRGR.', 'G.RGG.', '..GGR.', 'GRGGGG']) == 'G')
assert (findWinner(['GRR..G', 'R.R...', '....R.', '......', '...R..', 'GG....']) == '-')
assert (findWinner(['GRRRGG', 'RGR.R.', 'G.RRGR', 'G.GRRG', 'GRRGGR', '..RRGR']) == 'R')
assert (findWinner(['R.....', 'R.R...', '.G.GR.', '...R..', 'G.G...', '......']) == '-')
assert (findWinner(['.GGGGR', 'RGGRRG', 'RR...R', 'GR.GG.', '.G.RRG', 'R.GGRG']) == 'G')
assert (findWinner(['G..G.R', '..G...', '....G.', '.....G', 'R.R...', '......']) == '-')
assert (findWinner(['GGGG..', 'GRGRRR', 'G.GGGG', 'GGRRGG', 'GGGGGG', 'GR..RG']) == 'G')
assert (findWinner(['R.R...', '...R.G', '.R....', 'RR....', '......', '.GGR..']) == '-')
assert (findWinner(['GRGG..', 'G..GRG', 'GRRR.R', '..GRGR', '.GG.RR', '.GG.RR']) == 'R')
assert (findWinner(['..RR...', '.G..R..', '.......', '...RG..', '..R..G.', 'RR.R..R', 'R......']) == 'R')
assert (findWinner(['GRRG...', 'RRRGRRR', 'GGGRRG.', '.GGRGRR', 'G..GRRR', 'RRR.RRR', 'RRGGR.G']) == 'G')
assert (findWinner(['...G.G.', '..G..R.', '....G..', '....R.G', '...R..G', '....R..', '.....R.']) == '-')
assert (findWinner(['.GRRRG.', 'GR..RRG', 'GRGGRG.', 'GGGGGRR', 'R.GRGGG', '.RGR.GG', 'RRGGRGR']) == 'G')
assert (findWinner(['G..RG..', '.......', '.R.....', '.......', '......R', '.......', '.....G.']) == '-')
assert (findWinner(['GGRRGGR', 'RGGRR.R', 'RRG..GR', 'R.GG.GG', 'GR.GR.R', 'R.G..RR', 'RG.G..G']) == 'G')
assert (findWinner(['..G.GR.', '..R....', '.......', 'G.R.RR.', '.R..R.G', 'R.G....', 'R.G....']) == '-')
assert (findWinner(['GRRRRGG', 'RRRRGRG', 'RGGRGGR', 'RGGGRRR', 'G.RGGGR', '..GRR.R', 'GGRR.GR']) == 'R')
assert (findWinner(['...GG..', '...G...', 'R..G.G.', '..RG.R.', '.......', '..RR...', '..R.R..']) == 'G')
assert (findWinner(['GGR.RR.', 'R.GRGRR', '.GGGGR.', 'RGGG.GR', 'RGGGGRR', 'G.GRGGR', 'GRG.RGG']) == 'G')
assert (findWinner(['....R..', 'G...R..', '.......', 'GR.....', '..G....', '......R', '..RG.R.']) == '-')
assert (findWinner(['GRRR.R.', 'GGRRRGR', 'GRRR.GG', 'RRGGG.R', 'GGG.RGG', '.GR..GR', 'RRGGRGR']) == 'R')
