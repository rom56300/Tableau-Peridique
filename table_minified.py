A0='(294)'
z='(247)'
y='132.9054'
x='39.948'
w=str
i='arial'
h=list
g=int
a=' '
V='Méteaux alcalino-terreux'
U='Métaux Alcalins'
T='Gaz Nobles'
S='Métaloïdes'
P='Comic Sans MS'
N='Métaux Pauvres'
O=range
L='Inconnus'
I='Autres Non-Métaux'
H=True
G='Actinides'
F='Lanthanides'
B='Métaux de transition'
import sys,time,pygame as A
from os import environ as j
from pygame.constants import KEYDOWN as k,MOUSEBUTTONDOWN as l,QUIT as b
A.init()
A.display.set_caption(a)
J=219,227,230
m=0,0,0
n=1272
E=n/19
X=g(E*18+0.5)
Y=g(E*11+0.5)
K={0:['H','Hydrogène','1.00794',1,1,I],1:['He','Hélium','4.002602',18,1,T],2:['Li','Lithium','6.941',1,2,U],3:['Be','Béryllium','9.012182',2,2,V],4:['B','Bore','10.811',13,2,S],5:['C','Carbone','12.0107',14,2,I],6:['N','Azote','14.0067',15,2,I],7:['O','Oxygène','15.9994',16,2,I],8:['F','Fluor','18.9984032',17,2,I],9:['Ne','Néon','20.1797',18,2,T],10:['Na','Sodium','22.98976',1,3,U],11:['Mg','Magnésium','24.305',2,3,V],12:['Al','Aluminium','26.9815386',13,3,N],13:['Si','Silicon','28.0855',14,3,S],14:['P','Phosphore','30.973762',15,3,I],15:['S','Soufre','32.065',16,3,I],16:['Cl','Chlore','35.453',17,3,I],17:['Ar','Argon',x,18,3,T],18:['K','Potassium',x,1,4,U],19:['Ca','Calcium','40.078',2,4,V],20:['Sc','Scandium','44.955912',3,4,B],21:['Ti','Titanium','47.867',4,4,B],22:['V','Vanadium','50.9415',5,4,B],23:['Cr','Chrome','51.9961',6,4,B],24:['Mn','Manganèse','54.938045',7,4,B],25:['Fe','Fer','55.845',8,4,B],26:['Co','Cobalt','58.933195',9,4,B],27:['Ni','Nickel','58.6934',10,4,B],28:['Cu','Cuivre','63.546',11,4,B],29:['Zn','Zinc','65.38',12,4,B],30:['Ga','Gallium','69.723',13,4,N],31:['Ge','Germanium','72.63',14,4,S],32:['As','Arsenic','74.9216',15,4,S],33:['Se','Sélénium','78.96',16,4,I],34:['Br','Brome','79.904',17,4,I],35:['Kr','Krypton','83.798',18,4,T],36:['Rb','Rubidium','85.4678',1,5,U],37:['Sr','Strontium','87.62',2,5,V],38:['Y','Yttrium','88.90585',3,5,B],39:['Zr','Zirconium','91.224',4,5,B],40:['Nb','Niobium','92.90628',5,5,B],41:['Mo','Molybdène','95.96',6,5,B],42:['Tc','Technétium','(98)',7,5,B],43:['Ru','Ruthénium','101.07',8,5,B],44:['Rh','Rhodium','102.9055',9,5,B],45:['Pd','Palladium','106.42',10,5,B],46:['Ag','Argent','107.8682',11,5,B],47:['Cd','Cadmium','112.411',12,5,B],48:['In','Indium','114.818',13,5,N],49:['Sn','Étain','118.71',14,5,N],50:['Sb','Antimoine','121.76',15,5,S],51:['Te','Tellure','127.6',16,5,S],52:['I','Iode','126.90447',17,5,I],53:['Xe','Xenon','131.293',18,5,T],54:['Cs','Cesium',y,1,6,U],55:['Ba','Barium',y,2,6,V],56:['La','Lanthane','138.90547',4,9,F],57:['Ce','Cérium','140.116',5,9,F],58:['Pr','Praséodyme','140.90765',6,9,F],59:['Nd','Néodyme','144.242',7,9,F],60:['Pm','Prométhium','(145)',8,9,F],61:['Sm','Samarium','150.36',9,9,F],62:['Eu','Europium','151.964',10,9,F],63:['Gd','Gadolinium','157.25',11,9,F],64:['Tb','Terbium','158.92535',12,9,F],65:['Dy','Dysprosium','162.5',13,9,F],66:['Ho','Holmium','164.93032',14,9,F],67:['Er','Erbium','167.259',15,9,F],68:['Tm','Thulium','168.93421',16,9,F],69:['Yb','Ytterbium','173.054',17,9,F],70:['Lu','Lutétium','174.9668',18,9,F],71:['Hf','Hafnium','178.49',4,6,B],72:['Ta','Tantale','180.94788',5,6,B],73:['W','Tungstène','183.84',6,6,B],74:['Re','Rhénium','186.207',7,6,B],75:['Os','Osmium','190.23',8,6,B],76:['Ir','Iridium','192.217',9,6,B],77:['Pt','Platine','195.084',10,6,B],78:['Au','Or','196.966569',11,6,B],79:['Hg','Mercure','200.59',12,6,B],80:['Tl','Thallium','204.3833',13,6,N],81:['Pb','Plomb','207.2',14,6,N],82:['Bi','Bismuth','208.9804',15,6,N],83:['Po','Polonium','(209)',16,6,N],84:['At','Astate','(210)',17,6,S],85:['Rn','Radon','(222)',18,6,T],86:['Fr','Francium','(223)',1,7,U],87:['Ra','Radium','(226)',2,7,V],88:['Ac','Actinium','(227)',4,10,G],89:['Th','Thorium','232.03806',5,10,G],90:['Pa','Protactinium','231.0588',6,10,G],91:['U','Uranium','238.02891',7,10,G],92:['Np','Neptunium','(237)',8,10,G],93:['Pu','Plutonium','(244)',9,10,G],94:['Am','Americium','(243)',10,10,G],95:['Cm','Curium',z,11,10,G],96:['Bk','Berkélium',z,12,10,G],97:['Cf','Californium','(251)',13,10,G],98:['Es','Einstenium','(252)',14,10,G],99:['Fm','Fermium','(257)',15,10,G],100:['Md','Mendelévium','(258)',16,10,G],101:['No','Nobélium','(259)',17,10,G],102:['Lr','Lawrencium','(262)',18,10,G],103:['Rf','Rutherfordium','(267)',4,7,B],104:['Db','Dubnium','(268)',5,7,B],105:['Sg','Seaborgium','(271)',6,7,B],106:['Bh','Bohrium','(272)',7,7,B],107:['Hs','Hassium','(270)',8,7,B],108:['Mt','Meitnerium','(276)',9,7,L],109:['Ds','Darmstadium','(281)',10,7,L],110:['Rg','Roentgénium','(280)',11,7,L],111:['Cn','Copernicium','(285)',12,7,B],112:['Nh','Nihomium','(284)',13,7,L],113:['Fl','Flerovium','(289)',14,7,L],114:['Mc','Moscovium','(288)',15,7,L],115:['Lv','Livermorium','(293)',16,7,L],116:['Ts','Tennesine',A0,17,7,L],117:['Og','Oganesson',A0,18,7,L]}
c={0:['1s¹',1],1:['1s²',2],2:['[He] 2s¹',(2,1)],3:['[He] 2s²',(2,2)],4:['[He] 2s² 2p¹',(2,3)],5:['[He] 2s² 2p²',(2,4)],6:['[He] 2s² 2p³',(2,5)],7:['[He] 2s² 2p⁴',(2,6)],8:['[He] 2s² 2p⁵',(2,7)],9:['[He] 2s² 2p⁶',(2,8)],10:['[Ne] 3s¹',(2,8,1)],11:['[Ne] 3s²',(2,8,2)],12:['[Ne] 3s² 3p¹',(2,8,3)],13:['[Ne] 3s² 3p²',(2,8,4)],14:['[Ne] 3s² 3p³',(2,8,5)],15:['[Ne] 3s² 3p⁴',(2,8,6)],16:['[Ne] 3s² 3p⁵',(2,8,7)],17:['[Ne] 3s² 3p⁶',(2,8,8)],18:['[Ar] 4s¹',(2,8,8,1)],19:['[Ar] 4s²',(2,8,8,2)],20:['[Ar] 4s² 3d¹',(2,8,9,2)],21:['[Ar] 4s² 3d²',(2,8,10,2)],22:['[Ar] 4s² 3d³',(2,8,11,2)],23:['[Ar] 4s¹ 3d⁵',(2,8,12,2)],24:['[Ar] 4s² 3d⁵',(2,8,13,2)],25:['[Ar] 4s² 3d⁶',(2,8,14,2)],26:['[Ar] 4s² 3d⁷',(2,8,15,2)],27:['[Ar] 4s² 3d⁸',(2,8,16,2)],28:['[Ar] 4s¹ 3d¹⁰',(2,8,18,1)],29:['[Ar] 4s² 3d¹⁰',(2,8,18,2)],30:['[Ar] 4s² 3d¹⁰ 4p¹',(2,8,18,3)],31:['[Ar] 4s² 3d¹⁰ 4p²',(2,8,18,4)],32:['[Ar] 4s² 3d¹⁰ 4p³',(2,8,18,5)],33:['[Ar] 4s² 3d¹⁰ 4p⁴',(2,8,18,6)],34:['[Ar] 4s² 3d¹⁰ 4p⁵',(2,8,18,7)],35:['[Ar] 4s² 3d¹⁰ 4p⁶',(2,8,18,8)],36:['[Kr] 5s¹',(2,8,18,8,1)],37:['[Kr] 5s²',(2,8,18,8,2)],38:['[Kr] 5s² 4d¹',(2,8,18,9,2)],39:['[Kr] 5s² 4d²',(2,8,18,10,2)],40:['[Kr] 5s¹ 4d⁴',(2,8,18,12,1)],41:['[Kr] 5s¹ 4d⁵',(2,8,18,13,1)],42:['[Kr] 5s² 4d⁵',(2,8,18,13,2)],43:['[Kr] 5s¹ 4d⁷',(2,8,18,15,1)],44:['[Kr] 5s¹ 4d⁸',(2,8,18,16,1)],45:['[Kr] 4d¹⁰',(2,8,18,18)],46:['[Kr] 5s¹ 4d¹⁰',(2,8,18,18,1)],47:['[Kr] 5s² 4d¹⁰',(2,8,18,18,2)],48:['[Kr] 5s² 4d¹⁰ 5p¹',(2,8,18,18,3)],49:['[Kr] 5s² 4d¹⁰ 5p²',(2,8,18,18,4)],50:['[Kr] 5s² 4d¹⁰ 5p³',(2,8,18,18,5)],51:['[Kr] 5s² 4d¹⁰ 5p⁴',(2,8,18,18,6)],52:['[Kr] 5s² 4d¹⁰ 5p⁵',(2,8,18,18,7)],53:['[Kr] 5s² 4d¹⁰ 5p⁶',(2,8,18,18,8)],54:['[Xe] 6s¹',(2,8,18,18,8,1)],55:['[Xe] 6s²',(2,8,18,18,8,2)],56:['[Xe] 6s² 5d¹',(2,8,18,18,9,2)],57:['[Xe] 6s² 4f¹ 5d¹',(2,8,18,19,9,1)],58:['[Xe] 6s² 4f³',(2,8,18,21,8,2)],59:['[Xe] 6s² 4f⁴',(2,8,18,22,8,2)],60:['[Xe] 6s² 4f⁵',(2,8,18,23,8,2)],61:['[Xe] 6s² 4f⁶',(2,8,18,24,8,2)],62:['[Xe] 6s² 4f⁷',(2,8,18,25,8,2)],63:['[Xe] 6s² 4f⁷ 5d¹',(2,8,18,25,9,2)],64:['[Xe] 6s² 4f⁹',(2,8,18,27,8,2)],65:['[Xe] 6s² 4f¹⁰',(2,8,18,28,8,2)],66:['[Xe] 6s² 4f¹¹',(2,8,18,29,8,2)],67:['[Xe] 6s² 4f¹²',(2,8,18,30,8,2)],68:['[Xe] 6s² 4f¹³',(2,8,18,31,8,2)],69:['[Xe] 6s² 4f¹⁴',(2,8,18,32,8,2)],70:['[Xe] 6s² 4f¹⁴ 5d¹',(2,8,18,32,9,2)],71:['[Xe] 6s² 4f¹⁴ 5d²',(2,8,18,32,10,2)],72:['[Xe] 6s² 4f¹⁴ 5d³',(2,8,18,32,11,2)],73:['[Xe] 6s² 4f¹⁴ 5d⁴',(2,8,18,32,12,2)],74:['[Xe] 6s² 4f¹⁴ 5d⁵',(2,8,18,32,13,2)],75:['[Xe] 6s² 4f¹⁴ 5d⁶',(2,8,18,32,14,2)],76:['[Xe] 6s² 4f¹⁴ 5d⁷',(2,8,18,32,15,2)],77:['[Xe] 6s¹ 4f¹⁴ 5d⁹',(2,8,18,32,17,1)],78:['[Xe] 6s¹ 4f¹⁴ 5d¹⁰',(2,8,18,32,18,1)],79:['[Xe] 6s² 4f¹⁴ 5d¹⁰',(2,8,18,32,18,2)],80:['[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p¹',(2,8,18,32,18,3)],81:['[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p²',(2,8,18,32,18,4)],82:['[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p³',(2,8,18,32,18,5)],83:['[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁴',(2,8,18,32,18,6)],84:['[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁵',(2,8,18,32,18,7)],85:['[Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁶',(2,8,18,32,18,8)],86:['[Rn] 7s¹',(2,8,18,32,18,8,1)],87:['[Rn] 7s²',(2,8,18,32,18,8,2)],88:['[Rn] 7s² 6d¹',(2,8,18,32,18,9,2)],89:['[Rn] 7s² 6d²',(2,8,18,32,18,10,2)],90:['[Rn] 7s² 5f² 6d¹',(2,8,18,32,20,9,2)],91:['[Rn] 7s² 5f³ 6d¹',(2,8,18,32,21,9,2)],92:['[Rn] 7s² 5f⁴ 6d¹',(2,8,18,32,22,9,2)],93:['[Rn] 7s² 5f⁶',(2,8,18,32,24,8,2)],94:['[Rn] 7s² 5f⁷',(2,8,18,32,25,8,2)],95:['[Rn] 7s² 5f⁷ 6d¹',(2,8,18,32,25,9,2)],96:['[Rn] 7s² 5f⁹',(2,8,18,32,27,8,2)],97:['[Rn] 7s² 5f¹⁰',(2,8,18,32,28,8,2)],98:['[Rn] 7s² 5f¹¹',(2,8,18,32,29,8,2)],99:['[Rn] 7s² 5f¹²',(2,8,18,32,30,8,2)],100:['[Rn] 7s² 5f¹³',(2,8,18,32,31,8,2)],101:['[Rn] 7s² 5f¹⁴',(2,8,18,32,32,8,2)],102:['[Rn] 7s² 5f¹⁴ 7p¹',(2,8,18,32,32,8,3)],103:['[Rn] 7s² 5f¹⁴ 6d²',(2,8,18,32,32,10,2)],104:['[Rn] 7s² 5f¹⁴ 6d³',(2,8,18,32,32,11,2)],105:['[Rn] 7s² 5f¹⁴ 6d⁴',(2,8,18,32,32,12,2)],106:['[Rn] 7s² 5f¹⁴ 6d⁵',(2,8,18,32,32,13,2)],107:['[Rn] 7s² 5f¹⁴ 6d⁶',(2,8,18,32,32,14,2)],108:['[Rn] 7s² 5f¹⁴ 6d⁷',(2,8,18,32,32,15,2)],109:['[Rn] 7s² 5f¹⁴ 6d⁸',(2,8,18,32,32,16,2)],110:['[Rn] 7s² 5f¹⁴ 6d⁹',(2,8,18,32,32,17,2)],111:['[Rn] 7s² 5f¹⁴ 6d¹⁰',(2,8,18,32,32,18,2)],112:['[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p¹',(2,8,18,32,32,18,3)],113:['[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p²',(2,8,18,32,32,18,4)],114:['[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p³',(2,8,18,32,32,18,5)],115:['[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁴',(2,8,18,32,32,18,6)],116:['[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁵',(2,8,18,32,32,18,7)],117:['[Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁶',(2,8,18,32,32,18,8)]}
d={U:(229,116,188),V:(235,150,210),B:(249,180,237),N:(234,186,246),S:(220,179,255),I:(215,191,255),T:(196,199,255),F:(173,207,255),G:(150,215,255),L:(200,175,255)}
e=A.display.set_mode([X,Y])
D=A.display.get_surface()
C=h()
Q=A.Surface((X,Y))
Q.set_alpha(255)
Q.fill(J)
W=A.draw.rect(Q,J,(0,0,0,0),0)
Z=W
o,p=860,860
q=A.image.load('icon.png')
A.display.set_icon(q)
exit=W
def r():
	D.fill(J);N=56;Q=88
	for F in O(0,11):
		for B in O(0,18):
			if F==9 and B>2:C.insert(N,M(B,F));N+=1
			elif F==10 and B>2:C.insert(Q,M(B,F));Q+=1
			elif F==1 and(B<1 or B>16):C.append(M(B,F))
			elif F==2 and(B<2 or B>11):C.append(M(B,F))
			elif F==3 and(B<2 or B>11):C.append(M(B,F))
			elif 3<F<6:C.append(M(B,F))
			elif F==6 and(B<2 or B>2):C.append(M(B,F))
			elif F==7 and(B<2 or B>2):C.append(M(B,F))
			elif F==9 and B==1:K=A.draw.rect(D,J,(B*E,F*E,E,E),0);L=A.font.SysFont(P,20);G=L.render('LANTHANIDES',H,(0,0,0));I=G.get_rect();I.center=K.center;D.blit(G,I)
			elif F==10 and B==1:K=A.draw.rect(D,J,(B*E,F*E,E,E),0);L=A.font.SysFont(P,20);G=L.render('ACTINIDES',H,(0,0,0));I=G.get_rect();I.center=K.center;D.blit(G,I)
def M(i,j):global C;B=A.draw.rect(D,m,(i*E,j*E,E,E),1);return B
def s():
	A.font.init();I=A.font.SysFont(P,20);L=A.font.SysFont(i,9);M=A.font.SysFont(P,10);N=A.font.SysFont(P,10)
	for B in C:G=K[C.index(B)];A.draw.rect(D,d[G[5]],B,0);A.draw.rect(D,J,B,1)
	for B in C:G=K[C.index(B)];E=I.render(G[0],H,(0,0,0));F=E.get_rect();F.center=B.center;D.blit(E,F)
	for B in C:G=K[C.index(B)];E=L.render(G[1],H,(0,0,0));F=E.get_rect();F.midbottom=B.midbottom;D.blit(E,F)
	for B in C:G=K[C.index(B)];E=M.render(G[2].split('.')[0]+a,H,(0,0,0));F=E.get_rect();F.topright=B.topright;D.blit(E,F)
	for B in C:G=C.index(B)+1;E=N.render(a+w(G),H,(0,0,0));F=E.get_rect();F.topleft=B.topleft;D.blit(E,F)
def t():
	while H:
		for B in A.event.get():
			if B.type==b:sys.exit()
			elif B.type==l:
				D=A.mouse.get_pos()
				for E in C:
					if E.collidepoint(D):u(E)
					if W.collidepoint(D):v(c[C.index(Z)][1],K[C.index(Z)][0])
def u(rect):
	B=rect
	def F(recta):I=recta;global W,Z;G=A.draw.rect(D,d[K[C.index(I)][5]],(4*E,1*E,E*2,E*2),0);W=G;Z=I;A.font.init();N=A.font.SysFont(P,40);O=A.font.SysFont(i,18);Q=A.font.SysFont(P,20);R=A.font.SysFont(P,20);L=K[C.index(I)];B=N.render(L[0],H,(0,0,0));F=B.get_rect();F.center=G.center;D.blit(B,F);B=O.render(L[1],H,(0,0,0));F=B.get_rect();F.midbottom=G.midbottom;D.blit(B,F);B=Q.render(L[2].split('.')[0]+a,H,(0,0,0));F=B.get_rect();F.topright=G.topright;D.blit(B,F);L=C.index(I)+1;B=R.render(a+w(L),H,(0,0,0));F=B.get_rect();F.topleft=G.topleft;D.blit(B,F);G=A.draw.rect(D,J,(6*E,1*E,E*4,E*2),0);M=A.font.SysFont(P,20);B=M.render(K[C.index(I)][5],H,(0,0,0));F=B.get_rect();F.topleft=G.topleft;D.blit(B,F);B=M.render(K[C.index(I)][2]+' g/mol',H,(0,0,0));F=B.get_rect();F.midleft=G.midleft;D.blit(B,F);B=M.render(c[C.index(I)][0],H,(0,0,0));F=B.get_rect();F.bottomleft=G.bottomleft;D.blit(B,F)
	F(B);A.display.flip();A.draw.rect(D,(155,155,155),B,1);A.display.flip();time.sleep(0.2);A.draw.rect(D,J,B,1);A.display.flip()
def f():global C,e,D,Q;e=A.display.set_mode([X,Y]);D=A.display.get_surface();C=h();Q=A.Surface((X,Y));Q.set_alpha(255);Q.fill(J);A.draw.rect(D,(255,0,0),(550,450,100,50));C=h();r();s();A.display.flip();t();A.quit()
class R(A.sprite.Sprite):
	def __init__(B,pos,off,angle,*C):super().__init__(*C);B.image=A.Surface((20,20),A.SRCALPHA);A.draw.circle(B.image,(180,206,179),(10,10),10);B.rect=B.image.get_rect(center=pos);B.pos=A.math.Vector2(pos);B.offset=A.math.Vector2(off,0);B.angle=angle
	def update(A):A.angle-=0.25;A.rect.center=A.pos+A.offset.rotate(A.angle)
def v(conf_elec,symbol):
	B=conf_elec;global C;S=A.display.Info();j['SDL_VIDEO_WINDOW_POS']='{},{}'.format(S.current_w//2,S.current_h//2)
	if type(B)!=g:P=len(B)
	else:P=1
	if P==7:Q,G,I,J,K,L,M=B
	elif P==6:Q,G,I,J,K,L,M=B[0],B[1],B[2],B[3],B[4],B[5],0
	elif P==5:Q,G,I,J,K,L,M=B[0],B[1],B[2],B[3],B[4],0,0
	elif P==4:Q,G,I,J,K,L,M=B[0],B[1],B[2],B[3],0,0,0
	elif P==3:Q,G,I,J,K,L,M=B[0],B[1],B[2],0,0,0,0
	elif P==2:Q,G,I,J,K,L,M=B[0],B[1],0,0,0,0,0
	elif P==1:Q,G,I,J,K,L,M=B,0,0,0,0,0,0
	else:Q,G,I,J,K,L,M=0,0,0,0,0,0,0
	A.init();F=A.display.set_mode((o,p),A.NOFRAME|256);E=F.get_rect();W=A.time.Clock();N=A.sprite.Group();[R(E.center,100,A*180,N)for A in O(Q)];[R(E.center,150,A*(360/G),N)for A in O(G)];[R(E.center,200,A*(360/I),N)for A in O(I)];[R(E.center,250,A*(360/J),N)for A in O(J)];[R(E.center,300,A*(360/K),N)for A in O(K)];[R(E.center,350,A*(360/L),N)for A in O(L)];[R(E.center,400,A*(360/M),N)for A in O(M)]
	while H:
		for T in A.event.get():
			if T.type==b:sys.exit()
			elif T.type==k:f()
		A.font.init();X=A.font.SysFont(i,50);N.update();F.fill((64,86,98));Y=A.draw.circle(F,(250,212,216),E.center,60,0);U=X.render(symbol,H,(100,123,133));V=U.get_rect();V.center=Y.center;D.blit(U,V);A.draw.circle(F,(136,160,168),E.center,100,1)
		if G!=0:A.draw.circle(F,(136,160,168),E.center,150,1)
		if I!=0:A.draw.circle(F,(136,160,168),E.center,200,1)
		if J!=0:A.draw.circle(F,(136,160,168),E.center,250,1)
		if K!=0:A.draw.circle(F,(136,160,168),E.center,300,1)
		if L!=0:A.draw.circle(F,(136,160,168),E.center,350,1)
		if M!=0:A.draw.circle(F,(136,160,168),E.center,400,1)
		N.draw(F);A.display.flip();W.tick(288)
f()
