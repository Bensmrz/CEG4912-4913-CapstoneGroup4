import React from 'react';
import { View, FlatList, StyleSheet } from 'react-native';
import Message from './Message';

const chatData = [
  { id: '1', text: 'HI', timestamp: '2023-11-02T09:00:00Z', isUser: true },
  { id: '2', text: 'Heyyy!', timestamp: '2023-11-02T09:05:00Z', isUser: false },
  { id: '3', text: 'What\'s up?', timestamp: '2023-11-02T09:10:00Z', isUser: true }
];

const Chat = () => {
  return (
    <View style={styles.container}>
      <FlatList
        data={chatData.slice().reverse()}
        keyExtractor={(item) => item.id}
        inverted={true}
        renderItem={({ item }) => (
          <Message text={item.text} time={item.timestamp.slice(11, 16)} isUser={item.isUser} />
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});

export default Chat;
