import { question } from "readline-sync";

function cabecalho(){
    console.log('************BEM VINDO A CALCULADORA DE IAC************')
    console.log('------------------------------------------------------')
    console.log()
}

function rodape(){
    console.log()
    console.log('------------------------------------------------------')
    console.log('***********OBRIGADO! VOLTE SEMPRE, CUIDE-SE***********')
}

function input_dados(valores){
    const dados = Number(question(valores))
    return dados
}

function indice_ac(quadril, altura){ // calcular o indice adiposo corporal
    const iac = (((quadril / (altura * Math.sqrt(altura))) - 18) / 100)    //colocando o valor em Metros por isso a divisão por 100
    return iac
}

function cintura_min_normal(altura){ //calcular o valor maximo do quadril para o indice normal
    const calc_cintura_minima = (((altura * Math.sqrt(altura)) * (18 + 9)) / 100)  //colocando o valor em metros por isso a divisão por 100
    return calc_cintura_minima
}

function cintura_max_normal(altura){ //calcular o valor minimo do quadril para o indice normal
    const calc_cintura_maxima = (((altura * Math.sqrt(altura)) * (18 + 20.9)) / 100) //colocando o valor em metros por isso a divisão por 100
    return calc_cintura_maxima
}

function print(saida){ //Printar na tela o resultado
    console.log(saida)
}

function main(){
    cabecalho()
    
    //entrada
    const quadril = input_dados('Digite o comprimento de seu quadril em (cm): ')
    const altura = input_dados('Digite a sua altura em (cm): ')

    //processamento
    const indice_adiposidade = indice_ac(quadril, altura)
    const quadril_normal_min = cintura_min_normal(altura)
    const quadril_normal_max = cintura_max_normal(altura)

    //saida
    print('Confira a tabela do Indice de Adiposidade Corpotal')
    print(' Magra -> |0 À 8,9|\n Normal -> |9 À 20,9|\n Sobrepeso -> |21 À 25,9|\n Obesidade Grau 1 -> |26 À 29,9|')
    print(`O seu IAC foi de ${indice_adiposidade.toFixed(2)}`)
    print(`Caso você não esteja na faixa normal, aqui está o valor do quadril para se enquadrar: ${quadril_normal_min.toFixed(2)} minimo e ${quadril_normal_max.toFixed(2)} maximo`)
    
    rodape()
}
main()