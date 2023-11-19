import React from 'react';
import { View, StyleSheet } from 'react-native';
import Chat from '../assets/components/Chat';

export default function ChatLogs({ navigation }) {
  return (
    <View style={styles.container}>
      <Chat />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
