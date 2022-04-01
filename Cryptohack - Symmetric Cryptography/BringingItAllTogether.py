def decrypt(key, ciphertext):
    round_keys = expand_key(key) 
    state = bytes2matrix(ciphertext)
    state = add_round_key(state, round_keys[-1])

    for i in range(N_ROUNDS - 1, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        state = add_round_key(state, round_keys[i])
        inv_mix_columns(state)

    inv_shift_rows(state)
    inv_sub_bytes(state)
    state = add_round_key(state, round_keys[0])
    plaintext = matrix2bytes(state)

    return plaintext