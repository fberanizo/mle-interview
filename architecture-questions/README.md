## Nubank

Questões que eu elaborei antes da entrevista após assistir o vídeo [Nubank Data Science team and career](https://www.youtube.com/watch?v=8K6tS4xNrJU) e ler o [blog do Nubank](https://blog.nubank.com.br/tag/data-science/).

1. Como você criaria um modelo para decidir quem deve receber cartão de crédito (e quem não deve receber)?<br>
Objetivos de negócio: diminuir o risco, aumentar o número de pessoas aprovadas.

2. Como abordar o problema para decidir o limite de crédito dado a um cliente? E para decidir uma solicitação de aumento de crédito?<br>
Objetivos de negócio: criar modelos para aumentar/diminuir a exposição a riscos; aumentar o NPS (net promoter score); Long term metrics: O quanto se usa de um produto? O quanto se recomenda um produto (acho que este vale pra outras áreas tbm)
Fonte: https://blog.nubank.com.br/limite-cartao-nubank/
Quando alguém é aprovado para o cartão Nubank, fazemos uma projeção dos gastos dessa pessoa, análises de risco, perfil de uso e ainda usamos dados externos, como score (a pontuação usada pelo Serasa, que indica a probabilidade de as pessoas atrasarem ou não o pagamento de uma conta), por exemplo, para definir um patamar inicial e seguro de crédito.

Assim como acontece na nossa análise de aprovação de pedidos, um grande desafio na hora de estabelecer o limite é a falta de acesso a informações que nos ajudariam a traçar um perfil mais adequado.

Muitos dados fazem parte de um histórico privado construído entre as pessoas e as instituições financeiras.

dicas que podem te ajudar a aumentar o limite do cartão Nubank
Não atrasar o pagamento das faturas
Explorar bem o limite atual
Concentrar seus gastos no cartão Nubank
Evitar o crédito rotativo
Pagar o total da fatura até a data de vencimento
Manter sua renda atualizada no app do Nubank.

Na hora de definir o limite, analisamos também os dados a respeito do cliente em agências de crédito, o comportamento de compras e pagamentos, se há parcelamentos de fatura e se, em algum momento, o mesmo já teve dívidas com o Nubank.



3. Dado um dataset de informações de compra com cartão de crédito, com cada amostra rotulada como fraude/não-fraude, como construir um algoritmo de detecção de fraude?<br>

4. Risco de Crédito (quando a pessoa entra; após 3 meses; )<br>
como ela gasta dentro e fora do país; como cobrar uma pessoa que está atrasada no pagamento;
Objetivo de negócio: diminuir o risco. Cobrar melhor as pessoas;

5. Como construir um modelo para auto-reply de chat e email?<br>
Objetivos de negócio: aumentar eficiência das operações e manter um alto nível de satisfação do cliente. First response time. First contact to solution. 
Fonte: [Classificação de textos com Redes Neurais Convolucionais | Nubank ML Meetup](https://www.youtube.com/watch?v=TRhocAMGCfc)
*Pode ser necessário aplicar regras junto com ML (ex: cliente em atraso não recebe resposta)
Iterar no modelo (e na concepção do problema): aumentar o número de tópicos que consigo responder;
Problemas enfrentados: dados sem rótulo;
Posso utilizar embeddings pré-treinados + modelo de classificação.
O que pode dar errado?
É possível usar informação contextual. Ex: reissue-error, card-delivered, delivery error. 


6. Modelos para marketing. (pra quem eu ligo para tentar uma venda?)<br>

7. Imagine que uma empresa de telecomunicações entra em contato com você comentando que gostaria de saber a quais clientes deveria de ofertar um serviço adicional de internet. Você sabe que eles possuem uma base com um teste feito no passado para uma base aleatória de quais clientes receberam essa proposta e o resultado obtido do mesmo. Como você abordaria esse problema?<br>

8. 

Insumos:
- Datasets financeiros tem muita influência do tempo (ex: final de ano, FGTS, eleições...)
- [Nubank Data Science team and career | Nubank ML Meetup](https://www.youtube.com/watch?v=8K6tS4xNrJU)
- [Blog do Nubank](https://blog.nubank.com.br/tag/data-science/)
- [What's a useful model? Insights from a customer service perspective | Nubank Machine Learning Meetup](https://www.youtube.com/watch?v=LNe2m5Aw9gY)
Quando não usar modelos de ML (quando quiser minimizar erros custosos. ex: não deixar um modelo de nlp encerrar contas do Nubank). Quando tiver que manter transparência máxima sobre as decisões.
O que faz um bom produto de ML? Ver [](https://pair.withgoogle.com/guidebook/)
- Deixa claro o que é capaz de fazer (segue os modelos mentais dos clientes)
- Deixa claro porque fez (explicabilidade, leva em conta viéses sociais)
- Dá feedback, permite controle pelos usuários, aprende com comportamento do usuário
- Lida com falhas/erros gracefully

### Assuntos que um MLE precisa se preocupar
Nas provas de conceito:
- Criar hipóteses de negócio (qual o impacto do modelo)
- Estipular quais dados serão necessários (e como coletá-los, se necessário)
- Definir testes e experimentos
- Construir um modelo baseline: data prep., algoritmos, arquiteturas, optimizer, regularization, batch size, avaliação offline/online...
- Sugerir como utilizar o modelo em produção (Batch Job/Real Time? Shadow Mode/AB Testing...)
- Por quanto tempo validar o modelo?
- Gerar hipóteses do que pode dar errado (problemas com qualidade de dados, data e concept drift, ...)
- Decidir como monitorar o modelo em produção (métricas de negócio, de ML, de Software...)
- Como eu posso iterar nesse modelo e na concepção do problema/hipóteses? Preciso capturar mais dados? (ex: no problema de chat foi necessário capturar feedback explícito se o usuário ficou satisfeito)
- Como eu posso usar os dados que coletei nos testes. Existem problemas de feedback loop? (resposta do modelo em operação enviesa futuros modelos?)

Quando o modelo estiver em produção:
- Minimizar riscos de execução. 
- O modelo está funcionando direito? Tem alguma regra que está atrapalhando as coisas?
- O dado está sendo ingerido no lake/warehouse?
- Tem alguma informação faltando?
- O modelo está gerando scores adequadamente? 
- Está rodando rápido o suficiente?
- Se não for possível estimar um ganho com um modelo, sugerir caminhos para melhorar a estimativa de valor entregue pelo modelo: fazer pesquisas, rankear qual projeto é o mais importante;
- Qual o valor ganhado por atualizar o modelo (com mais dados, mais features)

## Outros
Casos de estudo retirados do [Machine Learning Systems Design](https://huyenchip.com/machine-learning-systems-design/toc.html).<br>

1. Duolingo is a platform for language learning. When a student is learning a new language, Duolingo wants to recommend increasingly difficult stories to read.
How would you measure the difficulty level of a story?
Given a story, how would you edit it to make it easier or more difficult?

2. Given a dataset of credit card purchases information, each record is labelled as fraudulent or safe, how would you build a fraud detection algorithm?

3. You run an e-commerce website. Sometimes, users want to buy an item that is no longer available. Build a recommendation system to suggest replacement items.

4. For any user on Twitter, how would you suggest who they should follow? What do you do when that user is new? What are some of the limitations of data-driven recommender systems?

5. When you enter a search query on Google, you're shown a list of related searches. How would you generate a list of related searches for each query?

6. Build a system that return images associated with a query like in Google Images.

7. How would you build a system to suggest trending hashtags on Twitter?

8. Each question on Quora often gets many different answers. How do you create a model that ranks all these answers? How computationally intensive is this model?

9. How to you build a system to display top 10 results when a user searches for rental listings in a certain location on Airbnb?

10. Autocompletion: how would you build an algorithm to finish your sentence when you text?

11. When you type a question on StackOverflow, you're shown a list of similar questions to make sure that your question hasn't been asked before. How do you build such a system?

12. How would you design an algorithm to match pool riders for Lyft or Uber?

13. On social networks like Facebook, users can choose to list their high schools. Can you estimate what percentage of high schools listed on Facebook are real? How do we find out, and deploy at scale, a way of finding invalid schools?

14. How would you build a trigger word detection algorithm to spot the word "activate" in a 10 second long audio clip?

15. If you were to build a Netflix clone, how would you build a system that predicts when a user stops watching a TV show, whether they are tired of that show or they're just taking a break?

16. Facebook would like to develop a way to estimate the month and day of people's birthdays, regardless of whether people give us that information directly. What methods would you propose, and data would you use, to help with that task?

17. Build a system to predict the language a text is written in.

18. Predict the house price for a property listed on Zillow. Use that system to predict whether we invest on buying more properties in a certain city.
19. Imagine you were working on iPhone. Everytime users open their phones, you want to suggest one app they are most likely to open first with 90% accuracy. How would you do that?

20. How do you map nicknames (Pete, Andy, Nick, Rob, etc) to real names?

21. An e-commerce company is trying to minimize the time it takes customers to purchase their selected items. As a machine learning engineer, what can you do to help them?

22. Build a chatbot to help people book hotels.

23. How would you design a question answering system that can extract an answer from a large collection of documents given a user query?

24. How would you train a model to predict whether the word "jaguar" in a sentence refers to the animal or the car?

25. Suppose you're building a software to manage the stock portfolio of your clients. You manage X amount of money. Imagine that you've converted all that amount into stocks, and find a stock that you definitely must buy. How do you decide which of your currently owned stocks to drop so that you can buy this new stock?

26. How would you create a model to recognize whether an image is a triangle, a circle, or a square?

27. Given only CIFAR-10 dataset, how to build a model to recognize if an image is in the 10 classes of CIFAR-10 or not?
