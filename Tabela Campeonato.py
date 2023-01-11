#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('corintias', 'palmeiras', 'santos', 'gremio',
         'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
         'atletico', 'botafogo', 'atletico=PR', 'bahia',
         'sao paulo', 'fluminece', 'sport recife', 'EC vitoria',
         'coritiba', 'avai', 'ponte preta', 'atletico-GO')
print(f'os 5 primeiros times sao {times[0:5]}')
print(f'os 4 ultimos colocados foram {times[-4:]}')
print(f'os times em ordem alfabetica sao {sorted(times)}')
print(f'o chapecoence esta em {times.index("chapecoense")} posicao')