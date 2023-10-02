import loadBalancer from "./7-load_balancer";

async function testLoadBalancer() {
  const chinaSuccess = 'Downloading from China is faster';
  const USASuccess = 'Downloading from USA is faster';

  const promiseChina = new Promise(function(resolve) {
    setTimeout(resolve, 100, chinaSuccess);
  });

  const promiseSlowChina = new Promise(function(resolve) {
    setTimeout(resolve, 500, chinaSuccess);
  });

  const promiseUSA = new Promise(function(resolve) {
    setTimeout(resolve, 300, USASuccess);
  });

  const value = await loadBalancer(promiseChina, promiseUSA);
  console.log(value); // Pour débogage
  if(value !== 'Downloading from China is faster') {
    throw new Error(`Expected 'Downloading from China is faster', but received ${value}`);
  }

  const value2 = await loadBalancer(promiseSlowChina, promiseUSA);
  console.log(value2); // Pour débogage
  if(value2 !== 'Downloading from USA is faster') {
    throw new Error(`Expected 'Downloading from USA is faster', but received ${value2}`);
  }
}

testLoadBalancer();
