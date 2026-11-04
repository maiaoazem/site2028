import assert from 'node:assert/strict';
import worker from '../worker.js';
const host='ctxt-humano-bionico.example';
const origin=`https://${host}`;
let stored=[];
const env={
  DB:{prepare(_sql){return{bind(...values){return{async run(){stored.push(values);return{success:true};}};}};}},
  ASSETS:{fetch:async()=>new Response('<h1>Site</h1>',{status:200})},
  DATA_CONTROLLER:'Organização Exemplo',PRIVACY_POLICY_URL:'https://example.com/privacidade',
  TURNSTILE_SITE_KEY:'site-test',TURNSTILE_SECRET_KEY:'secret-test',RETENTION_DAYS:'90'
};
const actualFetch=globalThis.fetch;
globalThis.fetch=async(url)=>{
  assert.equal(url,'https://challenges.cloudflare.com/turnstile/v0/siteverify');
  return Response.json({success:true,hostname:host});
};
const payload={schemaVersion:'1.1',name:'Pessoa Teste',company:'Empresa Teste',email:'pessoa@empresa.teste',
  privacyConsent:true,marketingConsent:false,aiTools:['ChatGPT'],turnstileToken:'test-token',
  answers:Array.from({length:20},(_,i)=>({number:i+1,raw:3}))};
const post=async(body)=>worker.fetch(new Request(`${origin}/api/lead`,{
  method:'POST',headers:{Origin:origin,'Content-Type':'application/json'},body:JSON.stringify(body)
}),env);
let config=await worker.fetch(new Request(`${origin}/api/config`),env);
assert.equal(config.status,200);
assert.equal((await config.json()).ready,true);
let response=await post(payload);
assert.equal(response.status,201);
let data=await response.json();
assert.equal(data.ok,true);
assert.equal(data.scores.xRaw,30);
assert.equal(data.scores.yRaw,30);
assert.equal(data.scores.quadrant,'high-high');
assert.equal(stored.length,1);
// A Q14 é afirmativa (não invertida), Q10 é a única invertida.
const modified=structuredClone(payload);
modified.answers[9].raw=1;
modified.answers[13].raw=5;
response=await post(modified);
assert.equal(response.status,201);
data=await response.json();
assert.equal(data.scores.xRaw,32);
assert.equal(data.scores.yRaw,32);
assert.equal(data.scores.x,55);
assert.equal(data.scores.y,55);
// Rejeições básicas de LGPD, e-mail e integridade.
assert.equal((await post({...payload,privacyConsent:false})).status,400);
assert.equal((await post({...payload,email:'teste@gmail.com'})).status,400);
assert.equal((await post({...payload,answers:payload.answers.slice(0,19)})).status,400);
assert.equal(stored.length,2);
// O token inválido não consegue gravar.
globalThis.fetch=async()=>Response.json({success:false,hostname:host});
assert.equal((await post(payload)).status,403);
assert.equal(stored.length,2);
globalThis.fetch=actualFetch;
console.log('OK: Worker validado (configuração, envio, pontuações, dados e Turnstile).');
