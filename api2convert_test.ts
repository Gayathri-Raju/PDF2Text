import fetch from 'node-fetch';
const myAPIKey="276a1999bf028071fb2f9e3300b89d9f"

const fet = async()=>{
  const res = await fetch('https://api.api2convert.com/v2/jobs', {
  method: 'POST',
  headers: {
    "X-Oc-Api-Key":  myAPIKey,
    'Content-Type': 'application/json'
  },
  body: '{"input": [{"type": "remote","source": "https://archive.nclt.gov.in/sites/default/files/Jan-final-orders-pdf/Alcon%20Consulting%20Engineers%20%28India%29%20Pvt%20Ltd%20%26%20Anr.pdf"}],"conversion": [{"target": "txt"}]}'
})
console.log(await res.json());
}

(async function() {
  await fet();
  //await get()
})();

const get = async()=>{
  fetch('https://api.api2convert.com/v2/jobs/', {
  method: 'GET',
  headers: {
    "Authorization": "X-Oc-Api-Key " + myAPIKey,
    'Content-Type': 'application/json',
    'Cache-Control':'no-cache'
  },
  body: '{"input": [{"type": "remote","source": "https://archive.nclt.gov.in/sites/default/files/Jan-final-orders-pdf/Alcon%20Consulting%20Engineers%20%28India%29%20Pvt%20Ltd%20%26%20Anr.pdf"}],"conversion": [{"target": "txt"}]}'
}).then(response => {
  console.log(response.json());
}).catch(err => {console.log(err);});
}
