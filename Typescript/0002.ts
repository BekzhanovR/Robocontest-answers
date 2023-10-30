import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function main() {
  rl.question('Enter two space-separated integers: ', (input: string) => {
    const numbers: number[] = input
      .split(' ')
      .map(s => parseInt(s, 10));

    const a: number = numbers[0];
    const b: number = numbers[1];

    const x: string = a > b ? '>' : a === b ? '=' : '<';
    console.log(x);

    rl.close();
  });
}

main();