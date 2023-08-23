document.addEventListener("DOMContentLoaded", function () {
    const calculateButton = document.getElementById("calculate-button");
    const pencilPurchase = document.getElementById("pencil-purchase");
    const penPurchase = document.getElementById("pen-purchase");
    const eraserPurchase = document.getElementById("eraser-purchase");
    const pencilSelling = document.getElementById("pencil-selling");
    const penSelling = document.getElementById("pen-selling");
    const eraserSelling = document.getElementById("eraser-selling");
    const remainingBalance = document.getElementById("remaining-balance");
  
    calculateButton.addEventListener("click", function () {
      const pencilPurchaseAmount = parseFloat(pencilPurchase.value);
      const penPurchaseAmount = parseFloat(penPurchase.value);
      const eraserPurchaseAmount = parseFloat(eraserPurchase.value);
  
      const pencilSellingAmount = parseFloat(pencilSelling.value);
      const penSellingAmount = parseFloat(penSelling.value);
      const eraserSellingAmount = parseFloat(eraserSelling.value);
  
      const totalPurchaseAmount = pencilPurchaseAmount + penPurchaseAmount + eraserPurchaseAmount;
      const totalSellingAmount = pencilSellingAmount + penSellingAmount + eraserSellingAmount;
  
      const calculatedBalance = totalSellingAmount - totalPurchaseAmount;
      remainingBalance.textContent = `$${calculatedBalance.toFixed(2)}`;
    });
  });
  