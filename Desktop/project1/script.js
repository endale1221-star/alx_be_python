let score = 20;
let highscore = 0;

let secretNumber = Math.trunc(Math.random() * 20) + 1;
console.log(secretNumber);

document.querySelector(".check").addEventListener("click", function () {
  let guess = Number(document.querySelector(".guess").value);
  console.log(guess, typeof guess);

  let displayMessage = function (message) {
    document.querySelector(".righth2").textContent = message;
  };

  //if guess is not
  if (!guess) {
    displayMessage("⛔ No Entry!");
  }

  // if the guess is exact
  else if (guess === secretNumber) {
    let hi;
    if (score > highscore) highscore = score;
    document.querySelector(".highNum").textContent = highscore;
    document.querySelector(".number").textContent = guess;

    displayMessage("🎉 Correct Number!");
    document.querySelector(".highNum").textContent = score;

    document.querySelector("*").style.backgroundColor = "green";
  }

  // if the guess is wrong
  else if (guess !== secretNumber) {
    if (score > 1) {
      guess > secretNumber
        ? displayMessage("Too High!")
        : displayMessage("Too Low!");
    } else {
      displayMessage("🔥 You Lose The Game!");
    }
  }

  // // if guess is greater
  // else if (guess > secretNumber) {
  //   if (score > 1) {
  //     displayMessage("Too High!");
  //     score--;
  //     document.querySelector(".scoreNum").textContent = score;
  //   } else {
  //     displayMessage("🔥 You Loss The Game!");
  //   }
  // }

  // //if the guess is smaller
  // else if (guess < secretNumber) {
  //   if (score > 1) {
  //     displayMessage("Too Low!");
  //     score--;
  //     document.querySelector(".scoreNum").textContent = score;
  //   } else {
  //     displayMessage("🔥 You Loss The Game!");
  //   }
  // }

  // play again button implementation

  document.querySelector(".playbutton").addEventListener("click", function () {
    score = 20;
    document.querySelector(".scoreNum").textContent = score;

    displayMessage("Starting Guessing...");
    document.querySelector(".number").textContent = "?";

    let secretNumber = Math.trunc(Math.random() * 20) + 1;
    console.log(secretNumber);

    document.querySelector("*").style.backgroundColor = "yellow";
    document.querySelector(".guess").value = "";
  });
});
