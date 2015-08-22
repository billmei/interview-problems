function reverse_words(message) {
	var words = message.split(' ');

	for (var i = 0; i < words.length / 2; i++) {
		var temp = words[i];
		words[i] = words[words.length - i - 1];
		words[words.length - i - 1] = temp;
	}

	return words.join(' ');
}