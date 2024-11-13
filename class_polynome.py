


class Polynome:
    def __init__(self,Px):
        self.Px=Px
    def afficher(self):
        for i in range(len(self.Px)):
            if (i == len(self.Px) - 1):
                if (self.Px[len(self.Px) - i - 1] >= 0):
                    print(str("+ ") + str(self.Px[len(self.Px) - i - 1]), end=" ")
                else:

                    print(str(self.Px[len(self.Px) - i - 1]), end=" ")

            elif (self.Px[len(self.Px) - i - 1] >= 0 and i > 0):
                print(str("+") + str(self.Px[len(self.Px) - i - 1]) + "X^" + str(len(self.Px) - i - 1), end=" ")
            elif (self.Px[len(self.Px) - i - 1] < 0 and i > 0):
                print(str(self.Px[len(self.Px) - i - 1]) + "X^" + str(len(self.Px) - i - 1), end=" ")
            else:
                print(str(self.Px[len(self.Px) - i - 1]) + "X^" + str(len(self.Px) - i - 1), end=" ")
        pass

    def get_valeur(self,x):

        s = x
        som = 0
        for i in range(len(self.Px)):
            for j in range(len(self.Px) - i - 1 - 1):
                s *= s
            if (i != len(self.Px) - 1):
                som = som + self.Px[len(self.Px) - i - 1] * s

            else:
                som = som + self.Px[len(self.Px) - i - 1]
            s = x
        print("\n" + "P(" + str(x) + ")=" + str(som))
        return som


px=Polynome([1,-4,2,-3,45,-5,0])

px.afficher()
px.get_valeur(0)
