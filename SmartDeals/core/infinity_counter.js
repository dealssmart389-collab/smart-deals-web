let currentStep = 1;
const infinity = Infinity;

export const evolutionProgress = () => {
  setInterval(() => {
    currentStep += Math.pow(currentStep, 1.1);
    console.log('مستوى اكتمال الكيان: ' + currentStep);
    if(currentStep >= infinity) console.log('تم بلوغ كمال المصفوفة');
  }, 500);
};