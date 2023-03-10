import { question } from "readline-sync";

//deixar o programa mais imersivo(visual) 
function cabecalho(){
    console.log('*********BEM VINDO(A) A CALCULADORA DE ÁGUA*********')
    console.log('----------------------------------------------------')
    console.log()
}

function rodape(){
    console.log()
    console.log('----------------------------------------------------')
    console.log('*********OBRIGADO, VOLTE SEMPRE. HIDRATE-SE!*********')
}

function print(resultado){
    //Printar o resultado no final
    console.log(resultado)
}

function input_numero(receber_numero){
    //entrada para valores
    const numero = Number(question(receber_numero))
    return numero
}

function atividade_moderada(peso){
    //calculo para atividade moderada
    const valor_agua_moderada = (peso * 35) / 1000
    return valor_agua_moderada
}

function atividade_intensa(peso){
    //calculo para atividade intensa
    const valor_agua_intenso = (peso * 45) / 1000
    return valor_agua_intenso
}


function main(){
    cabecalho()

    //entrada 
    const peso = input_numero('##### > Por favor, digite o seu peso (kg): ' )
     
    //processamento
    const exercicio_moderado = atividade_moderada(peso)
    const exercicio_intenso = atividade_intensa(peso)


    //saida
    print(`\n-> Para atividades fisicas moderadas, o ideal é a ingestão de ${exercicio_moderado.toFixed(2)}L de água.`)
    print(`-> Para atividades fisicas intensas, o ideal é a ingestão de ${exercicio_intenso.toFixed(2)}L de água.`)
    
    rodape()
}
main()