X_list, y_list = mlp_data_preprocess("/content/drive/MyDrive/AI_music/AI Music Data/", "/content/drive/MyDrive/AI_music/Real Music Data/")

X = np.array(X_list)
y = np.array(y_list)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.15, random_stat
model = Sequential()
model.add(Dense(1000, input_shape=(9997,), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(400, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])



X_list, y_list = lstm_data_preprocess("/content/drive/MyDrive/AI_music/AI Music Data/", "/content/drive/MyDrive/AI_music/Real Music Data/")

X = np.transpose(np.array(X_list),(0,2,1))
y = np.array(y_list)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.15, random_state = 42)
lstm_model = Sequential()
lstm_model.add(LSTM(200, return_sequences= True, input_shape=(769,13)))
lstm_model.add(Dropout(0.2))
lstm_model.add(LSTM(80, return_sequences = False))
lstm_model.add(Dropout(0.2))
lstm_model.add(Dense(20, activation = 'relu'))
lstm_model.add(Dense(1, activation='sigmoid'))

lstm_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
lstm_model.fit(X_train,y_train, epochs = 15, validation_data = (X_test, y_test))


class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super().__init__()
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)

num_heads = 8
ff_dim = 16
inputs = layers.Input(shape=(769,13))
transformer_block = TransformerBlock(13, num_heads, ff_dim)
x = transformer_block(inputs)
x = layers.GlobalAveragePooling1D()(x)
x = layers.Dropout(0.3)(x)
x = layers.Dense(50, activation="relu")(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(2, activation="softmax")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
history = model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))

 








