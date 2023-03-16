/* TMB (taxa metabolica basal) é a quantidade de energia necessária para a manutenção das funções vitais do organismo ao longo de 24 horas.
é medida em calorias, que é a energia extraída pelo nosso corpo a partir dos macronutrientes (carboidratos, proteínas e gorduras totais).*/

import { question } from "readline-sync";
 //deixar o programa mais imersivo (visualmente) cabeçalho e rodapé.
function cabecalho(){
    console.log('**********Bem vindo a calculadora de TMB**********')
    console.log('--------------------------------------------------')
    console.log()
}

function rodape(){
    console.log()
    console.log('--------------------------------------------------')
    console.log('*************Obrigado! Volte sempre.**************')  
}

function input_dados(entrada){
    //receber valores numericos
    const dados = Number(question(entrada))
    return dados 
}

function input_sexo(entrada2){
    //receber valores em letra (string)
    const letra = String(question(entrada2))
    return letra
    }

function tmb_homem(peso, altura, idade){
    //calcular a taxa de metabolica masculina
    const metabolica_masc = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    return metabolica_masc
}

function print(mostrar_resultado){
    //jogar o valor na tela(vulgo printar)
    console.log(mostrar_resultado)
}

/*function tmb_mulher(peso, altura, idade){
    //calcular a taxa de metabolica feminina
    const metabolica_fem = 447.6 + ((9.2 * peso) + (3.1 * altura) - (4.3 * idade))
    return metabolica_fem
}*/

function main (){
    cabecalho()
    //entrada
    const peso = input_dados('Digite seu peso em (kg): ')
    const altura = input_dados('Digite sua altura em (cm): ')
    const idade = input_dados('Digite sua Idade (anos): ')
    const sexo = input_sexo('Digite Seu sexo (M) para masculino ou (F) para feminino: ') //entrada para string
    
    //processamento
    const tmb_masculino = tmb_homem(peso, altura, idade)

    //saida
    print(` ->Peso: ${peso}\n ->Altura: ${altura}\n ->Idade: ${idade}\n ->Sexo: ${sexo}\n A taxa metabolica basal de um homem com as caracteristicas definidas anteriormente são: ${Math.floor(tmb_masculino)}.`)
   
    rodape()
}

main()