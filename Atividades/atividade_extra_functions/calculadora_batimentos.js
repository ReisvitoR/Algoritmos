import { question } from "readline-sync";

//deixa o programa mais imersivo (visual)
function cabecalho(){
    console.log()
    console.log('**************BEM VINDO(A) A CALCULADORA DE BATIMENTOS CARDÍACOS**************')
    console.log('----------------------------------------------------------------------------------')
    console.log()
}

//deixa o programa mais imersivo (visual)
function rodape(){
    console.log()
    console.log('----------------------------------------------------------------------------------')
    console.log('**************************OBRIGADO, VOLTE SEMPRE. CUIDE-SE!**************************')
}

//Recebe entrada
function input_numero(receber_numero){
    const numero = Number(question(receber_numero))
    return numero
}

//Calcula a frequencia cardiaca maxima geral
function frequencia_cardiaca_max (idade){
    const frequencia_max = 220 - idade
    return frequencia_max
}

//calcula a frequencia cardiaca minima para exercicios fisicos moderados
function frequencia_cardiaca_moderada_min(idade){
    const frequencia_moderada = frequencia_cardiaca_max(idade) 
    const frequencia_moderada_min = Math.floor (0.5 * frequencia_moderada)
    return frequencia_moderada_min
}

//calcula a frequencia cardiaca maxima para exercicio fisicos moderados
function frequencia_cardiaca_moderada_max(idade){
    const frequencia_moderada = frequencia_cardiaca_max(idade)
    const frequencia_moderada_max = Math.floor( 0.7 * frequencia_moderada)
    return frequencia_moderada_max
}

//calcula a frequencia cardiaca minima para exercicio fisicos intensos
function frequencia_cardiaca_intensa_min(idade){
    const frequencia_intensa = frequencia_cardiaca_max(idade)
    const frequencia_intensa_min = Math.floor(0.7 * frequencia_intensa)
    return frequencia_intensa_min
}

//calcula a frequencia cardiaca maxima para exercicio fisicos intensos
function frequencia_cardiaca_intensa_max(idade){
    const frequencia_intensa = frequencia_cardiaca_max(idade)
    const frequencia_intensa_max = Math.floor(0.85 * frequencia_intensa)
    return frequencia_intensa_max
}

//mostra o resultado final na tela
function print(resultado){
    console.log(resultado)
}

function main(){
    cabecalho()
    
    //entrada
    const idade = input_numero('#####> Por favor, digite a sua Idade: ')

    //processamento
    const frequencia_cardiaca_maxima = frequencia_cardiaca_max(idade)
    const frequencia_moderada_minima = frequencia_cardiaca_moderada_min(idade)
    const frequencia_moderada_maxima = frequencia_cardiaca_moderada_max(idade)
    const frequencia_intensa_minima = frequencia_cardiaca_intensa_min(idade)
    const frequencia_intensa_maxima = frequencia_cardiaca_intensa_max(idade)

    //saida
    print(`\n-> A sua frequencia cardiaca máxima deverá ser: ${frequencia_cardiaca_maxima}bpm`)
    print(`-> Para exercicios fisicos moderados a sua frequencia minima deverá ser: ${frequencia_moderada_minima}bpm`)
    print(`-> Para exercicios fisicos moderados a sua frequencia máxima deverá ser: ${frequencia_moderada_maxima}bpm`)
    print(`-> Para exercicios fisicos intensos a sua frequencia minima deverá ser: ${frequencia_intensa_minima}bpm`)
    print(`-> Para exercicios fisicos intensos a sua frequencia máxima deverá ser: ${frequencia_intensa_maxima}bpm`)

    rodape()
}
main()