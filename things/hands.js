const hands = () => {
  const html = document.querySelector("html");
  
  const hands = ["grab", "grabbing"];
  let currentHandIdx = 0;
  
  const newTimeoutSet = () => {
    const numTimes = Math.floor(Math.random() * 12) + 3;
    const timeInterval = Math.floor(Math.random() * 700) + 150;
    for (let i = 0; i < numTimes; i++) {
      setTimeout(() => {
        currentHandIdx = (currentHandIdx + 1) % hands.length;
        html.style.cursor = hands[currentHandIdx];
        if (i === numTimes - 1) setTimeout(newTimeoutSet, timeInterval);
      }, (timeInterval * i));
    }
  }
  
  newTimeoutSet();
}

hands();