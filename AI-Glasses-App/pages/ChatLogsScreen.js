import React from 'react';
import { View, StyleSheet } from 'react-native';
import Chat from '../assets/components/Chat';

function ChatLogsScreen({ navigation }) {
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

export default ChatLogsScreen;