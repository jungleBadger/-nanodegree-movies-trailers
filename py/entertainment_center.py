import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "test", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtube.com/watch?v=vwyZH85NQC4")
o_invasor = media.Movie("O Invasor", "O INVASOR narra a historia de tres amigos companheiros desde os tempos de faculdade de engenharia que sao socios em uma construtora ha mais de 15 anos. Tudo corre bem ate o dia em que um desentendimento na conducao dos negocios os coloca em conflito", "https://upload.wikimedia.org/wikipedia/pt/b/b8/O_Invasor.jpg", "https://www.youtube.com/watch?v=O4wZgt0eiWg")
things_i_hate = media.Movie("10 Things I Hate About You", "A pretty, popular teenager can't go out on a date until her ill-tempered older sister does.", "https://upload.wikimedia.org/wikipedia/pt/7/76/10_Things_I_Hate_About_You.jpg", "https://www.google.com.br/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjNhJTnjcrQAhUBEZAKHWYjD8QQtwIIIDAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAWmjzCZr0Jw&usg=AFQjCNESEvQOoFrbwr8JCtGAFt93mg_UOg&sig2=uqpeFb3bNKv661sl84legg")
sucker_punch = media.Movie("Sucker Punch", "A young girl is institutionalized by her abusive stepfather. Retreating to an alternative reality as a coping strategy, she envisions a plan which will help her escape from the mental facility.", "https://upload.wikimedia.org/wikipedia/en/9/9f/Sucker_Punch_film_poster.jpg", "https://www.google.com.br/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjKsaOCjsrQAhVCx5AKHWpyCrwQuAIIITAA&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DXAnnWoXD2tI&usg=AFQjCNFd67-yrLugqZ2QJ20GlSw5LucCIg&sig2=9MVngMZhY5PVKAIXUSpAqQ")
carandiru = media.Movie("Carandiru", "Brazilian MD Drauzio Varella starts AIDS prevention in Brazil's largest prison, Carandiru, in Sao Paulo, where the population is nearly double its 4,000 maximum.", "https://filmesnobrasil.files.wordpress.com/2013/07/carandiru.jpg", "https://www.youtube.com/watch?v=5C0mR2tfWMU")
sunshine_mind = media.Movie("Eternal Sunshine of the Spotless Mind", "When their relationship turns sour, a couple undergoes a procedure to have each other erased from their memories. But it is only through the process of loss that they discover what they had to begin with.", "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg", "https://www.youtube.com/watch?v=yE-f1alkq9I")

movies = [toy_story, o_invasor, things_i_hate, sucker_punch, carandiru, sunshine_mind]

fresh_tomatoes.open_movies_page(movies)