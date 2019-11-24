var prev = parseInt(document.getElementById('opening_balance').innerHTML)
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

function formatDate(date) {
  var monthNames = [
    "January", "February", "March",
    "April", "May", "June", "July",
    "August", "September", "October",
    "November", "December"
  ];

  var day = date.getDate();
  var monthIndex = date.getMonth();
  var year = date.getFullYear();

  return day + ' ' + monthNames[monthIndex] + ' ' + year;
}

document.getElementById('date-tab').innerHTML = formatDate(new Date())
