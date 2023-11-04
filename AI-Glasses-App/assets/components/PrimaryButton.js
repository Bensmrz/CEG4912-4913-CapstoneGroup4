import React from 'react';
import { Text, StyleSheet } from 'react-native';
import { Button } from '@rneui/themed';

export default function PrimaryButton(props) {
  const { text, onPress } = props;
  return (
    <Button buttonStyle={styles.button} onPress={onPress}>
      <Text style={styles.buttonText}>{text}</Text>
    </Button>
  );
}

const styles = StyleSheet.create({
  button: {
    width: 130,
    padding: 10,
    borderRadius: 30,
    alignItems: 'center'
  },
  buttonText: {
    fontSize: 16,
    color: 'white' 
  },
});
