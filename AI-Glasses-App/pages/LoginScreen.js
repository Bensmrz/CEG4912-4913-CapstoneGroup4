import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';
import { StyleSheet, View, TextInput, Text } from 'react-native';
import CreateAccountButton from './../assets/components/CreateAccountButton';
import PrimaryButton from './../assets/components/PrimaryButton'

function LoginScreen({ navigation }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    if (username === 'username' && password === 'password') {
      console.log('Login successful');
    } else {
      console.log('Login failed');
    }
  };

  return (
    <View style={styles.container}>
      <Text>Login</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        onChangeText={text => setUsername(text)}
        value={username}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        onChangeText={text => setPassword(text)}
        value={password}
      />
      <View style={styles.signupContainer}>
        <PrimaryButton text="Login" onPress={handleLogin} />
        <CreateAccountButton text="Create Account" onPress={handleLogin}/>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  heading: {
    fontSize: 24,
    marginBottom: 20,
  },
  input: {
    width: 200,
    height: 40,
    borderWidth: 1,
    borderColor: 'gray',
    marginBottom: 10,
    padding: 10
  },
  signupContainer: {
    marginTop: 5,
    alignItems: 'center',
    gap: 10,
    display: 'flex'
  },
});

export default LoginScreen;