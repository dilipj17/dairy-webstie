var prev = 0
for (var i = 1;; i++) {
  var amount = document.getElementById(i+'-amount');
  if(amount){
    if (parseInt(amount.dataset.credit,10)) {
      prev += parseInt(amount.dataset.amount,10);
    }
    else{
      prev -= parseInt(amount.dataset.amount,10);
    }
    document.getElementById(i+'-balance').innerHTML = prev;
    if (prev < 0) {
      document.getElementById(i+'-balance').style.color = 'red'
    }
  }
  else{
    break;
  }
}
