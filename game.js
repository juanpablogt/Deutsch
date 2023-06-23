var vocabulario_semana_1 = {
    "Guten Morgen": "Buenos días",
    "Hallo": "Hola",
    "Wie geht es dir?": "¿Cómo estás?",
    "Ich heiße...": "Me llamo...",
    "Woher kommst du?": "¿De dónde eres?"
};

var palabras = [ "Guten Morgen", "Hallo", "Wie geht es dir?", "Ich heiße...", "Woher kommst du?" ];
var jugadores = [ "Juan", "María", "Pedro"];
var puntajes = { "Juan": 0, "María": 0, "Pedro": 0 };

function startGame() {
    var playerName = document.getElementById("player-name").value;

    if (playerName.trim() === "") {
        alert("Por favor, ingresa un nombre de jugador válido.");
        return;
    }

    jugadores.push(playerName);
    puntajes[playerName] = 0;

    document.getElementById("player-name").value = "";
    document.getElementById("player-name").focus();

    document.getElementById("player-list").innerHTML = jugadores.join(", ");
    
    document.getElementById("player-name").disabled = true;
    document.getElementById("start-button").disabled = true;
    document.getElementById("game-button").disabled = false;
}

function nextWord() {
    var word = getRandomWord();
    document.getElementById("word").innerHTML = word;
    document.getElementById("answer").value = "";
    document.getElementById("answer").focus();
}

function getRandomWord() {
    var keys = Object.keys(vocabulario_semana_1);
    var randomIndex = Math.floor(Math.random() * keys.length);
    return keys[randomIndex];
}

function checkAnswer() {

    var word = document.getElementById("word").innerHTML;
    var answer = document.getElementById("answer").value;
    var correctAnswer = vocabulario_semana_1[word];

    if (answer === correctAnswer) {
        alert("¡Correcto!");
        puntajes[jugadores[0]] += 1;
    } else {
        alert("¡Incorrecto! La respuesta correcta es: " + correctAnswer);
    }

    document.getElementById("score").innerHTML = puntajes[jugadores[0]];
    nextWord();
}

function endGame() {
    var winner = jugadores[0];
    var maxScore = puntajes[winner];

    for (var i = 1; i < jugadores.length; i++) {
        var score = puntajes[jugadores[i]];
        if (score > maxScore) {
            winner = jugadores[i];
            maxScore = score;
        }
    }

    alert("¡El ganador es " + winner + " con " + maxScore + " puntos!");
    resetGame();
}

function resetGame() {
    jugadores = [];
    puntajes = {};

    document.getElementById("player-name").disabled = false;
    document.getElementById("start-button").disabled = false;
    document.getElementById("game-button").disabled = true;

    document.getElementById("player-name").focus();
    document.getElementById("player-list").innerHTML = "";
    document.getElementById("score").innerHTML = "0";
    document.getElementById("word").innerHTML = "";
    document.getElementById("answer").value = "";
}

