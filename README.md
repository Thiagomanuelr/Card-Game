# Card-Game

## Como jogar

O projeto usa Python, Tkinter e Pillow. Para iniciar:

```bash
python main.py
```

No menu inicial:

1. Entre em **DECKS** para consultar os decks, comprar cartas ou criar um deck personalizado.
2. Entre em **JOGAR**, escolha uma região e selecione o deck.
3. Na preparação, o oponente começa com dois monstros de custo 1 ou 2 que compartilham pelo menos uma tag.
4. O jogador começa com 3 moedas. Arraste cartas da área de compra para preparar seus campos.
5. Quando estiver pronto, clique em **COMEÇAR COMBATE**.
6. Durante seu turno, clique em um personagem seu e depois em um personagem inimigo para atacar. Cada personagem pode atacar uma vez por turno.
7. Clique em **ENCERRAR TURNO** para passar a vez ao oponente. O oponente ataca automaticamente e os turnos se alternam.

O combate termina quando todos os personagens de um dos lados forem destruídos. Ao entrar em uma nova fase, o oponente coloca uma quantidade de monstros igual à quantidade da fase anterior mais um. As cartas que o jogador colocou em campo são mantidas; apenas as cartas que ainda estavam disponíveis para compra voltam para o deck, que é embaralhado antes de comprar cinco novas cartas.

Comprar, jogar ou equipar uma carta não repõe automaticamente a área de compra. Essa área representa a mão do jogador: cada fase começa com cinco cartas na mão, mas ela comporta até dez cartas quando passivas adicionam cartas extras.

O campo do oponente comporta no máximo cinco monstros. Quando a fase gerar mais monstros, os excedentes ficam na reserva e entram automaticamente no campo assim que um espaço for liberado.

Uma partida tem no máximo 18 fases e não possui limite de turnos. Nas fases 6, 12 e 18 aparece um chefe de custo 6 ou 8 com HP igual ao HP base triplicado mais 10 vezes o número do turno atual. Se o jogador perder enquanto um chefe estiver ativo, perde a partida. Derrotar um chefe antes da fase 18 inicia a próxima fase; derrotar o chefe da fase 18 vence a partida.

Para equipar uma arma, arraste uma carta do tipo **Weapon** diretamente sobre um personagem no campo. Cada arma equipada concede +50 de poder e +50 de HP ao personagem.

Se um personagem do jogador for destruído em combate, ele retorna ao campo na próxima fase com seu HP restaurado, incluindo os bônus de armas equipadas. Ao invocar um personagem sobre outro personagem do seu campo, o personagem que estava no local é destruído.

O jogador começa a partida com 80 de vida. Cada derrota em combate causa 15 de dano mais o número de fases já concluídas (na fase 1 são 15, na fase 2 são 16, e assim por diante). Ao perder um combate, o jogador recebe 3 moedas extras para a próxima fase.

Vitórias consecutivas concedem moedas extras para a fase seguinte: a primeira vitória seguida concede 1 moeda, a segunda concede 2, e assim por diante. Uma derrota reinicia a sequência de vitórias. A partida termina quando a vida do jogador chega a zero.

## Passivas

As passivas das cartas dos decks iniciais `deck` e `deck2` são acionadas automaticamente ao jogar a carta, iniciar o combate, descartar uma carta da mão ou destruir um personagem. Efeitos de compra, busca, cura, bônus de poder/HP, redução de custo, destruição, retorno do descarte, vínculo e ataques adicionais já participam da partida.

Quando uma passiva exige uma escolha que ainda não possui uma interface própria, o jogo usa uma regra determinística: escolhe a primeira carta elegível do deck ou descarte e, para alvos inimigos, prioriza o alvo com maior poder ou o primeiro alvo elegível.

Use o botão **DESCARTE** durante a partida para consultar as cartas descartadas, as cartas destruídas e os personagens destruídos que retornarão ao campo na próxima fase.

Passivas com `+cost por turno` concedem moedas adicionais para a próxima fase. Passivas com `-cost` reduzem o custo das cartas correspondente; `Fake Sky` aplica a redução temporariamente às cartas inimigas durante três turnos.

## Dependências

Instale o Pillow caso ainda não esteja disponível:

```bash
python -m pip install Pillow
```