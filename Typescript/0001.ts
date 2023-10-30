import fs from 'fs';

const data: string = fs.readFileSync(0, 'utf-8');

const [a, b] = data.split(' ').map(x => parseInt(x, 10));
process.stdout.write('' + (a + b));