//"Programa" que calcula o tempo com base na distancia e velocidade 

import { question } from "readline-sync";

function cabecalho(){
    console.log('***CÁLCULO DA PROVA DE TEMPO OU CORRIDA ***')
    console.log('__________________________________________')
    console.log()
}

function rodape(){
    console.log()
    console.log('___________________________________________')
    console.log('**********OBRIGADO, VOLTE SEMPRE!**********')
}

function input_valor(entrada){
    const dados = Number(question(entrada))
    return dados
}

function calc_tempo (distancia, velocidade){
    const tempo = (distancia / (velocidade * 1000)) * 60
    return tempo
}

function print(saida){
    console.log(saida)
} 
function main(){
    cabecalho()
    //entrada
    const distancia = input_valor('Digite a distancia em (M): ')
    const velocidade = input_valor('Digite a Velocidade em (km/h): ')
    
    //processamento
    const tempo_resultado = calc_tempo(distancia, velocidade)

    //saida
    print(` A prova ou caminhada teve duração de ${tempo_resultado} minutos, foram ${distancia} metros percorridos por uma velocidade de ${velocidade}km/h `)
    rodape()
}
main()