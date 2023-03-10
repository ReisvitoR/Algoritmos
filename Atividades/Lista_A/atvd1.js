import {question} from 'readline-sync'

// Entrada
const velocidade_ms = Number(question('Velocidade (m/s): '))

// Processamento
const velocidade_kmh = (velocidade_ms * 3.6)

// Saida
console.log(velocidade_ms, 'm/s equivale a ', velocidade_kmh, 'em km/h')

