<?php

function caesarCipher($text, $shift, $mode = 'encrypt') {
    $result = '';
    $shift = $mode === 'encrypt' ? $shift : -$shift;

    for ($i = 0; $i < strlen($text); $i++) {
        $char = $text[$i];
        
        if (ctype_alpha($char)) {
            $ascii = ord(strtoupper($char));
            $shifted = ($ascii - 65 + $shift + 26) % 26 + 65;
            $newChar = chr($shifted);
            
            $result .= ctype_upper($char) ? $newChar : strtolower($newChar);
        } else {
            $result .= $char;
        }
    }

    return $result;
}

// Contoh penggunaan
$plaintext = "KRIPTOGRAFI";
$shift = 5;

$encrypted = caesarCipher($plaintext, $shift, 'encrypt');
echo "Teks asli: $plaintext\n";
echo "Teks terenkripsi: $encrypted\n";

$decrypted = caesarCipher($encrypted, $shift, 'decrypt');
echo "Teks terdekripsi: $decrypted\n";
?>