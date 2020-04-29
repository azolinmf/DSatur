class dsatur:
	V = [] #Vertices
	T = {} #Vizinhos
	d_satur = {}
	#O grau d de cada vertice é len(T[])
	
	disponivel = {}
	cor ={}
	
	def criaVertice(self, v):
		self.V += [v]
		self.T[v] = []
		self.d_satur[v] = 0
		self.cor[v] = None
	def addAresta(self, a, b):
		if not a in self.V:
			self.criaVertice(a)
		if not b in self.V:
			self.criaVertice(b)
		self.T[a]+=[b]
		self.T[b]+=[a]
		
	def escolher(self):
		u = -1
		for i in self.V:
			if self.disponivel[i]:
				if u is -1:
					u=i
				elif self.d_satur[i]>self.d_satur[u]:
					u=i
				elif self.d_satur[i]==self.d_satur[u] and len(self.T[i]) > len(self.T[u]):
					u=i
		return u
		
	def DSATUR_ALGORITHM(self):
		for u in self.V:
			self.disponivel[u]=True
		
		while True in self.disponivel.values():
			u = self.escolher()
			print('Escolhido:',u)
			self.disponivel[u]=False
			
			cores_disponiveis = ['rosa', 'azul', 'verde', 'lilás']	
			
			for vizinho in self.T[u]:
				self.d_satur[vizinho]+=1
				if self.cor[vizinho] in cores_disponiveis:
					cores_disponiveis.remove(self.cor[vizinho])
					print('Vizinho:',vizinho,' cor:',self.cor[vizinho])
			
			print('Cores:',cores_disponiveis)
			self.cor[u] = cores_disponiveis[0]	
			print(u,':',self.cor[u])
			print()
			
	def __init__(self):
		################## Entrada #####################
		#try:
		print('Programa DSATUR')
		arq = open('entrada.csv', 'r')
		print('Arquivo aberto!')
		for linha in arq:
			linha = linha.replace(' ', '').replace('\n', '')
			a, b = linha.split(',')
			self.addAresta(a, b)
		arq.close()
		#except:
		#		print('Não foi possível abrir o arquivo!')		
		self.imprimir()
		################################################
		
		
		################ CALCULAR DSATUR ###############
		self.DSATUR_ALGORITHM()
		################################################
		
		
		################# SALVAR SAIDA #################
		print('Salvando Saida...')
		arq = open('saida.csv', 'w')
		#arq.write('No. nós,No. arestas,Grau dos nós,,,,No. Cores,Run
		for v, c in self.cor.items():
			print(v,c)
		arq.close()
		################################################
		
	def imprimir(self):
		print()
		for i in self.V:
			print('Vertice:', i)
			print('Vizinhos:', self.T[i])
			print('Grau de Saturação:', self.d_satur[i])
			print('Grau:', len(self.T[i]))
			print()
	

dsatur()
