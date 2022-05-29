class Biblioteka:
    def __init__(self):
      self.egzemplarze=[]
      self.wypozyczenia=[]
      self.czytelnicy=[]
      self.ksiazki=[]
      self.tytuly=[]

    def dostepne_egz(self, tytul):
      for i in self.egzemplarze:
        if i.tytul==tytul:
          o=(i.tytul, i.autor, i.rok_wydania)
          print(o)

    def dostepne_ks(self):
      for i in self.ksiazki:
        count=self.egzemplarze.count(i.tytul)
        t=(i.tytul, i.autor, count)
        print(t)


    def dodaj_egz(self, tl, al, r_wl):
        c=self.tytuly.count(tl)
        if c==0:
            self.dodaj_ks(tl, al)

        print(c)
        for e in self.ksiazki:
            if e.tytul==tl:
                nowy=Egzemplarz(e.tytul, e.autor, r_wl)
                self.egzemplarze.append(nowy)


    def dodaj_ks(self, tytul, autor):
      nowa=Ksiazka(tytul, autor)
      self.ksiazki.append(nowa)
      self.tytuly.append(nowa.tytul)

class Ksiazka:
      def __init__ (self, tytul, autor):
        self.tytul=tytul
        self.autor=autor

class Egzemplarz:
  def __init__(self, tytul, autor, rok_wydania):
    self.tytul=tytul
    self.autor=autor
    self.rok_wydania=rok_wydania
    self.wypozyczony=bool(False)

  def __repr__(self):

    return (self.tytul, self.autor, self.rok_wydania)


nowa_Biblioteka=Biblioteka()

liczba_egzemplarzy=int(input())
for e in range(0,liczba_egzemplarzy):
  ex=eval(input())
  nowa_Biblioteka.dodaj_egz(ex[0], ex[1], ex[2])

nowa_Biblioteka.dostepne_ks()

